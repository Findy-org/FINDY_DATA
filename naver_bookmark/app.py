from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

class LinkInput(BaseModel):
    url: str

@app.post("/api/naver_bookmark")
async def get_bookmarks_from_url(link: LinkInput):
    if not link.url.startswith("https://naver.me/"):
        raise HTTPException(status_code=400, detail="Invalid Naver short link format.")

    # 입력 받은 url에서 shareId 추출.
    try:
        async with httpx.AsyncClient(follow_redirects=True) as client:
            response = await client.get(link.url)
            final_url = str(response.url)
            share_id = extract_share_id_from_url(final_url)
            if not share_id:
                raise HTTPException(status_code=400, detail="ShareId not found in the URL.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching or processing the URL: {str(e)}")

    # 네이버 api를 사용해서 shareId로 북마크 상세정보 추출.
    # 아래 url은 Naver API URl 주소.
    api_url = f"https://pages.map.naver.com/save-pages/api/maps-bookmark/v3/shares/{share_id}/bookmarks?start=0&limit=5000&sort=lastUseTime"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url)
            response.raise_for_status()
            bookmarks_data = response.json()

            # 장소명, 위도, 경도, 주소, 카테고리
            bookmarks = [
                {
                    "id": index + 1,
                    "title": item["name"],
                    "category": item["mcidName"],
                    "address": item["address"],
                    "mapx": str(item["px"]),
                    "mapy": str(item["py"])
                }
                for index, item in bookmarks_data.get("bookmarkList", [])
            ]

            return {"shareId": share_id, "bookmarks": bookmarks}
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Request error: {str(e)}")
    except KeyError as e:
        raise HTTPException(status_code=500, detail=f"Key error: {str(e)}")

# 입력 받은 url에서 shareId 추출
def extract_share_id_from_url(url: str) -> str:
    import re
    match = re.search(r"folder/([a-zA-Z0-9]+)", url)
    if match:
        return match.group(1)
    return None
