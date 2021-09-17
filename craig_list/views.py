import requests

from bs4 import BeautifulSoup
from requests.compat import quote_plus
from django.shortcuts import render

# Create your views here.

BASE_YOUTUBE_SEARCH_URL = "https://www.youtube.com/results?search_query={}"


def home(request):
    return render(request,'craig_list/base.html')


def search(request):

    search_value = ''
    test = ''
    # res = requests.get(YOUTUBE_SEARCH_URL)
    # test = res.content

    # if request.method == "POST":
    #     search_value = request.POST.get('search')

    test = {
        't' : test,
        'search_value' : search_value
    }
    
    
    return render(request,'craig_list/search.html',test)

def test(request):
    return render(request,'craig_list/base.html')