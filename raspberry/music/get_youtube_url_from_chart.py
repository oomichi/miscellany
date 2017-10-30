from apiclient.discovery import build
from apiclient.errors import HttpError
import billboard
import httplib
from oauth2client.tools import argparser

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(youtube, keyword):
    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        order="viewCount",
        maxResults=1).execute()

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] != "youtube#video":
            continue
        print("https://www.youtube.com/watch?v=%s"
              % search_result["id"]["videoId"])


if __name__ == "__main__":
    argparser.add_argument("--api-key",
                           help="the API key value from the APIs & auth of "
                           "https://cloud.google.com/console . Ensure you "
                           "have enabled the YouTube Data API.")
    args = argparser.parse_args()

    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=args.api_key)
    except httplib.ResponseNotReady:
        print("Need to specify a valid API key with --api-key option.")
        exit(1)

    chart = billboard.ChartData('hot-100')
    for song in chart:
        keyword = "%s %s" % (song.title, song.artist)
        youtube_search(youtube, keyword)
