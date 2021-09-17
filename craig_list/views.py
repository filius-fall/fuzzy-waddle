import requests
import json

from bs4 import BeautifulSoup
from requests.compat import quote_plus
from django.shortcuts import render

from decouple import config
from .youtube_id import recent_youtube_video


# Create your views here.

BASE_YOUTUBE_SEARCH_URL = "https://www.youtube.com/results?search_query={}"


API_KEY = config('YOUTUBE_API_KEY')
COREY_CHANNEL_ID = config("COREY_CHANNEL_ID")
LINKS = json.loads(config("VIDEO_LINKS"))


def home(request):
    return render(request,'craig_list/base.html')


def search(request):


    # res = requests.get(YOUTUBE_SEARCH_URL)
    # test = res.content

    # if request.method == "POST":
    #     search_value = request.POST.get('search')

    youtube_base_url = "https://www.youtube.com/embed/"
    
    # YOUTUBE_LINK = youtube_base_url + youtube_video_id

    # EMBEDED_LINK = "https://www.youtube.com/embed/" + youtube_video_id

    dict_links = {}

    for i in LINKS:
        dict_links[i] = youtube_base_url + recent_youtube_video(API_KEY,LINKS[i])
        # video_id.append(i)

    test = {
        'dict_links' : dict_links,
    }
    
    
    return render(request,'craig_list/search.html',test)

def test(request):
    return render(request,'craig_list/base.html')