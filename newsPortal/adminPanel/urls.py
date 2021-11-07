from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^ap/index/$', views.ap_index, name="apIndex"),
    re_path(r'^ap/home/$', views.ap_home, name="apHome"),

    re_path(r'^ap/remove/user/(?P<pk>\d+)/$', views.ap_removeUser, name="apRemoveUser"),

    # News Cateory ########################################
    # add news category
    re_path(r'^ap/add/news/category/$', views.ap_add_news_category, name="apAddNewsCategory"),
    # delete news category
    re_path(r'^ap/del/news/category/(?P<pk>\d+)/$', views.ap_delete_news_category, name="apDelNewsCat"),
    # edit news category
    re_path(r'^ap/edit/news/category/(?P<pk>\d+)/$', views.ap_edit_news_category, name="apEditNewsCat"),

    # see subcategories by categories
    re_path(r'^ap/newscats/subcat/list/(?P<news_cat_id>\d+)/$', views.apNewsCats_subcategories, name="apNewsCatsSubcatList"),

    # delete subcategories
    re_path(r'^ap/del/news/subcat/by/news/cat/(?P<news_subcat_id>\d+)/$', views.apNewsCats_DelSubcategories, name="apDelNewsSubcatByNewsCat"),

    # News Subcategory #####################################
    re_path(r'^ap/add/news/subcat/$', views.ap_add_news_sub_category, name='apAddNewsSubCat'),

    # edit news subcat
    re_path(r'^ap/edit/news/subcat/(?P<subcat_id>\d+)/$', views.apEditNewsSubcat, name="apEditNewsSubcat"),

    # delete news subcat
    re_path(r'^ap/del/news/subcat/(?P<subcat_pk>\d+)/$', views.apDelNewsSubcat, name="apDelNewsSubCat"),


    # add news ################################################################
    re_path(r'^ap/add/news/$', views.ap_addNews, name="apAddNews"),

    # news list
    re_path(r'^ap/news/list/$', views.ap_newsList, name="apNewsList"),

    # delete news
    re_path(r'^ap/del/news/(?P<news_id>\d+)/$', views.ap_delNews, name="apDelNews"),

    # edit news
    re_path(r'^ap/edit/news/(?P<news_id>\d+)/$', views.ap_editNews, name="apEditNews"),

    # add news editor ########################################################
    re_path(r'^ap/add/news/editor/$', views.ap_addNewsEditor, name="apAddNewsEditor"),

    # delete news editor
    re_path(r'^ap/del/news/editor/(?P<pk>\d+)/$', views.ap_delNewsEditor, name="apDelNewsEditor"),
    # delete news editor
    re_path(r'^ap/edit/news/editor/(?P<pk>\d+)/$', views.ap_editNewsEditor, name="apEditNewsEditor"),

    # News Publisher name #####################################################
    re_path(r'^ap/add/news/publisher/$', views.ap_addNewsPublisher, name="apAddNewsPublisher"),

    # delete news publisher
    re_path(r'^ap/del/news/pubslisher/(?P<pk>\d+)/$', views.ap_delNewsPublisher, name="apDelNewsPusblisher"),

    # edit news poblisher
    re_path(r'^ap/edit/news/publisher/(?P<pk>\d+)/$', views.ap_editNewsPublisher, name="apEditNewsPublisher"),


    # breaking news#####################################
    re_path(r'^ap/add/breaking/news/$', views.ap_addBreakingNews, name="apAddBreakingNews"),

    # delete breaking news
    re_path(r'^ap/del/breaking/news/(?P<news_id>\d+)/$', views.ap_delBreakingNews, name="apDelBreakingNews"),

    # edit breaking news
    re_path(r'^ap/edit/breaking/news/(?P<news_id>\d+)/$', views.ap_editBreakingNews, name="apEditBreakingNews"),

    # add site logo ############################################
    re_path(r'^ap/add/site/logo/$', views.ap_addSiteLogo, name="apAddSiteLogo"),

    # delete site logo
    re_path(r'^ap/del/site/logo/(?P<logo_id>\d+)/$', views.ap_delSiteLogo, name="apDelSiteLogo"),

    # edit site logo
    re_path(r'^ap/edit/site/logo/(?P<logo_id>\d+)/$', views.ap_editSiteLogo, name="apEditSiteLogo"),

    # site contact info
    re_path(r'^ap/add/site/contact/info/$', views.ap_addSiteContactInfo, name="apAddSiteContactInfo"),

    # site contact info
    re_path(r'^ap/add/site/contact/info/bangla/$', views.ap_addSiteContactInfoBangla, name="apAddSiteContactInfoBangla"),
    re_path(r'^ap/del/site/contact/info/bangla/(?P<pk>\d+)/$', views.ap_deleteSiteContactInfoBangla, name="apDeleteSiteContactInfoBangla"),
    re_path(r'^ap/edit/site/contact/info/bangla/(?P<pk>\d+)/$', views.ap_editSiteContactInfoBangla, name="apEditSiteContactInfoBangla"),

    # delete contact info
    re_path(r'^ap/del/site/contact/info/(?P<contact_id>\d+)/$', views.ap_delSiteContactInfo, name="apDelSiteContactInfo"),

    # edit contact info
    re_path(r'^ap/edit/site/contact/info/(?P<contact_id>\d+)/$', views.ap_editSiteContactInfo, name="apEditSiteContactInfo"),


    # news gallery ########################################################################################################
    re_path(r'^ap/news/gallery/$', views.ap_newsGallery, name="apNewsGallery"),
    re_path(r'^ap/news/gallery/list/$', views.ap_news_GalleryList, name="apNewsGalleryList"),
    re_path(r'^ap/news/gallery/images/(?P<gallery_id>\w+)/$', views.ap_news_GalleryImages, name="apNewsGalleryImages"),

    re_path(r'^ap/del/gallery/(?P<gallery_id>\w+)/$', views.ap_deleteNewsGallery, name="apDelNewsGallery"),

    # custom ads section ###################################################################################################
    re_path(r'^ap/news/add/custom/ads/$', views.ap_addCustomAds, name="apAddCustomAds"),
    re_path(r'^ap/news/del/custom/ads/(?P<ads_id>\d+)/$', views.ap_deleteCustomAds, name="apDeleteCustomAds"),

    #  about us
    re_path(r'^ap/news/about/us/$', views.ap_aboutUs, name="apAboutUs"),
    re_path(r'^ap/del/news/about/us/(?P<pk>\d+)/$', views.ap_delAboutUs, name='apDelAboutUs'),
    re_path(r'^ap/del/news/about/us/edit/(?P<pk>\d+)/$', views.ap_editAboutUs, name='apEditAboutUs'),

    # msg list
    re_path(r'^ap/visitor/msg/list/$', views.ap_VisitorMsgList, name="apVisitorMessageList"),

    re_path(r'^ap/del/visitor/msg/(?P<pk>\d+)/$', views.ap_DelVisitorMsg, name="apDelVisitorMsg"),

    #************integrate social media link
    re_path(r'^ap/add/social/media/link/$', views.ap_addSocialMediaLink, name="apAddSocialMediaLink"),
    re_path(r'^ap/del/social/media/link/(?P<pk>\d+)/$', views.ap_delSocialMediaLink, name="apDelSocialMediaLink"),
    re_path(r'^ap/edit/social/media/link/(?P<pk>\d+)/$', views.ap_editSocialMediaLink, name="apEditSocialMediaLink"),


]
