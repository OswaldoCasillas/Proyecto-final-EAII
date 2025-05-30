import os
import re
from dotenv import load_dotenv
from googleapiclient.discovery import build
import csv




load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")  # Use YOUTUBE_API_KEY in your .env



youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_channel_id(channel_query):
    search_request = youtube.search().list(
        part='snippet',
        q=channel_query,
        type='channel',
        maxResults=1
    )
    search_response = search_request.execute()
    return search_response['items'][0]['snippet']['channelId']

def get_videos_from_channel(channel_id, max_results=30):
    videos_request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        maxResults=max_results,
        order='date',
        type='video'
    )
    videos_response = videos_request.execute()
    return [
        {
            'video_id': item['id']['videoId'],
            'video_title': item['snippet']['title']
        }
        for item in videos_response['items']
    ]

def get_comments(video_id, video_title, max_comments=500):
    comments = []
    next_page_token = None
    while len(comments) < max_comments:
        try:
            request = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=500,
                pageToken=next_page_token,
                textFormat='plainText'
            )
            response = request.execute()
            for item in response['items']:
                comment_id = item['id']
                comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append({
                    'comment_id': comment_id,
                    'comment': comment_text,
                    'video_id': video_id,
                    'video_title': video_title
                })
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
        except Exception as e:
            print(f"Error fetching comments for video {video_id}: {e}")
            break
    return comments

def main():



    channel_query = 'Morat'
    channel_id = get_channel_id(channel_query)
    print(f"Channel ID: {channel_id}")

    videos = get_videos_from_channel(channel_id)
    print(f"Found {len(videos)} videos.")

    all_comments = []
    for i, video in enumerate(videos, 1):
        print(f"Scraping comments from video {i}/{len(videos)}: {video['video_title']}")
        video_comments = get_comments(
            video_id=video['video_id'],
            video_title=video['video_title'],
            max_comments=500  
        )
        all_comments.extend(video_comments)

    print(f"Total comments collected: {len(all_comments)}")
    if len(all_comments) < 500:
        print("Warning: Less than 500 comments scraped. Try increasing max_comments or add more videos.")




    os.makedirs('data', exist_ok=True)
    csv_file = 'data/dataset.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['comment_id', 'comment', 'video_id', 'video_title']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_comments)
    print(f"CSV file created: {csv_file} with {len(all_comments)} comments.")

if __name__ == '__main__':
    main()
