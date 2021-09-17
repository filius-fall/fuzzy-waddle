
from googleapiclient.discovery import build





def recent_youtube_video(api_key,channel_id):

    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=1,
            order="date"
            
        )
    response = request.execute()

    return response.get('items')[0].get('id').get('videoId')


# from decouple import config
# API_KEY = config('YOUTUBE_API_KEY')
# COREY_CHANNEL_ID = config("COREY_CHANNEL_ID")
# k = recent_youtube_video(API_KEY,COREY_CHANNEL_ID)
# print(k)
