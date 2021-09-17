from django.urls import path
from . import views

app_name="craig_list"
urlpatterns = [
    path("",views.home,name="home"),
    path("search/",views.search,name="search"),
    path("test/", views.test, name="test")
]