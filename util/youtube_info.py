import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")
video_id = 'SG6fP8f2FkA'
youtube_api_url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}".format(video_id = video_id, api_key = api_key)
response = requests.get(youtube_api_url)
dict_response = response.json()
print(json.dumps(dict_response, indent=4, ensure_ascii=False, sort_keys=True))

video_title = dict_response['items'][0]['snippet']['title']
channel_name = dict_response['items'][0]['snippet']['channelTitle']
video_description = dict_response['items'][0]['snippet']['description']
channel_id = dict_response['items'][0]['snippet']['channelId']

print(video_title)
print(video_description)
print(channel_name)
print(channel_id)


