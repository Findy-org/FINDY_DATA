# Normal Url
# https://www.youtube.com/watch?v=video_id
#
# Share Url
# https://youtu.be/video_id
#
# Share Url with start time
# https://youtu.be/video_id?t=6
#
# Mobile browser url
# https://m.youtube.com/watch?v=video_id&list=RDvideo_id&start_radio=1
#
# Long url
# https://www.youtube.com/watch?v=video_id&list=RDvideo_id&start_radio=1&rv=smKgVuS
#
# Long url with start time
# https://www.youtube.com/watch?v=video_id&list=RDvideo_id&start_radio=1&rv=video_id&t=38
#
# Youtube Shorts
# https://youtube.com/shorts/video_id

import re


def validate_youtube_url(url):
    patterns = {
        "Normal URL": r"^https:\/\/(www\.)?youtube\.com\/watch\?v=[\w-]{11}$",
        "Share URL": r"^https:\/\/youtu\.be\/[\w-]{11}$",
        "Share URL with Start Time": r"^https:\/\/youtu\.be\/[\w-]{11}\?t=\d+$",
        "Mobile Browser URL": r"^https:\/\/m\.youtube\.com\/watch\?v=[\w-]{11}(&\S*)?$",
        "Long URL": r"^https:\/\/(www\.)?youtube\.com\/watch\?v=[\w-]{11}(&\S*)?$",
        "Long URL with Start Time": r"^https:\/\/(www\.)?youtube\.com\/watch\?v=[\w-]{11}(&\S*)?&t=\d+$",
        "YouTube Shorts": r"^https:\/\/(www\.)?youtube\.com\/shorts\/[\w-]{11}$"
    }

    for url_type, pattern in patterns.items():
        if re.match(pattern, url):
            return f"Valid {url_type}"
    return "Invalid YouTube URL"


# Test cases
test_urls = [
    "https://www.youtube.com/watch?v=SG6fP8f2FkA",
    "https://youtu.be/SG6fP8f2FkA",
    "https://youtu.be/SG6fP8f2FkA?t=6",
    "https://m.youtube.com/watch?v=SG6fP8f2FkA&list=RDSG6fP8f2FkA&start_radio=1",
    "https://www.youtube.com/watch?v=SG6fP8f2FkA&list=RDSG6fP8f2FkA&start_radio=1&rv=smKgVuS",
    "https://www.youtube.com/watch?v=SG6fP8f2FkA&list=RDSG6fP8f2FkA&start_radio=1&rv=SG6fP8f2FkA&t=38",
    "https://youtube.com/shorts/SG6fP8f2FkA"
]

for url in test_urls:
    print(f"{url} -> {validate_youtube_url(url)}")