from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^fe/index/$', views.front_index, name="frontEndIndex"),
    re_path(r'^$', views.front_home, name="frontEndHome"),
    re_path(r'^fe/news/details=616ab6a2-11d7-4a46-b89c-276e3fea887d/(?P<pk>\d+)/$', views.front_news_details, name='frontEndNewsDetails'),
    re_path(r'^fe/news/list=616ab6a2-11d7-4a46-b89c-276e3fea887d/(?P<pk>\d+)/$', views.front_news_list, name='frontEndNewsList'),
    # news list of single subcat
    re_path(r'^fe/news/list/subcategory/(?P<pk>\d+)/$', views.front_news_list_subcat, name='frontEndNewsListSubcat'),

    re_path(r'^fe/news/contact/$', views.front_contact, name='frontEndContact'),
    re_path(r'^fe/search/news/region/$', views.front_searchNewsByRegion, name='frontEndSearchNewsByRegion'),

    re_path(r'^fe/search/news/list/$', views.front_searhResult, name='frontEndSearchResult'),

]
