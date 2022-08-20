# Youtube Current Trending : Enter country and returns top 10 current trending videos

from googleapiclient.discovery import build
import pycountry

api_key = "AIzaSyCSdtXwwN3yrfIl0gwle_yG8ifI-mlx25A"
youtube = build('youtube','v3', developerKey=api_key)

entered_country = "India"
for country in pycountry.countries:
    try:
        if country.name == entered_country:
            iso_code = country.alpha_2 
    except KeyError:
            iso_code = "IN"


videos=[]

vd_request = youtube.videos().list(
        part = ["snippet","statistics"],
        chart = "mostPopular",
        regionCode = iso_code
    )

vd_response = vd_request.execute()

for item in vd_response["items"]:
    vid_views = item['statistics']['viewCount']
    vid_id = item['id']
    vid_title = item["snippet"]["title"]
    yt_link = f"https://youtu.be/{vid_id}"

    videos.append(
        {
            "views" : int(vid_views),
            "url" : yt_link,
            "title": vid_title
        }
    )


videos.sort(key=lambda vid: vid['views'],reverse=True)

for video in videos[:10]:
    print(video['url'],video['views'],video['title'])
# vid_request = youtube.videos().list(
#         part = ["statistics","snippet"],
#         id= ','.join(vid_ids)
#     )

  