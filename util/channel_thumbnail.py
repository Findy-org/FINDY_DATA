
import requests
import json
import os
from dotenv import load_dotenv

from util.youtube_info import channel_id


def get_channel_thumbanail(channel_id):
    load_dotenv()
    api_key = os.environ.get("GOOGLE_API_KEY")
    # channel_id = 'UC86GzuZXRb7aZnhnnUA3IAg'

    youtube_api_url = "https://www.googleapis.com/youtube/v3/channels?part=snippet&fields=items%2Fsnippet%2Fthumbnails%2Fdefault&id={channel_id}&key={api_key}".format(channel_id = channel_id, api_key = api_key)
    response = requests.get(youtube_api_url)
    dict_response = response.json()
    print(json.dumps(dict_response, indent=4, ensure_ascii=False, sort_keys=True))


    thumbnail_url = dict_response['items'][0]['snippet']['thumbnails']['default']['url']
    print(thumbnail_url)

if __name__ == '__main__':
    channel_id = 'UC86GzuZXRb7aZnhnnUA3IAg'
    get_channel_thumbanail(channel_id)

