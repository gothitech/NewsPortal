from django.shortcuts import render, redirect, get_object_or_404
from adminPanel.models import *
from .models import CustomAds
from django.contrib import messages
from django.db.models import Q


# index
def front_index(request):

    # breaking news
    breaking_news = BreakingNews.publishedObjects.filter().first()

    # sponsored ads at slider
    onload_ads = CustomAds.onload_ads.filter().order_by('-pk')[:2]

    # sponsored ads at header/top
    ads_header = CustomAds.onheader_ads.filter().order_by('-pk').first()


    # sponsored ads at middle
    ads_middle_position = CustomAds.onmiddle_ads.filter().order_by('-pk').first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    # news category
    news_category_list = NewsCategory.objects.filter()[:10]

    # news category all
    news_category_all = NewsCategory.objects.all()

    # about us
    about_us = AboutUs.objects.filter().first()

    # NewsEditorNameList
    newsEditorNameList = NewsEditorNameList.objects.filter().first()

    # NewsPublisherList
    newsPublisherList = NewsPublisherList.objects.filter().first()


    context = {
        # onload ads
        'onload_ads' : onload_ads,

        # ads at header/top
        'ads_header' : ads_header,

        # site logo
        'site_logo': site_logo,

        # news category
        'news_category_list' : news_category_list,

        # news_category_all
        'news_category_all' : news_category_all,

        # about us
        'about_us': about_us,

        # NewsEditorNameList
        'newsEditorNameList' : newsEditorNameList,

        # NewsPublisherList
        'newsPublisherList' : newsPublisherList,

        # breaking news
        'breaking_news': breaking_news,
    }

    return render(request, 'front-end/index.html', context)

# home
def front_home(request):

    # news category
    news_category_list = NewsCategory.objects.filter()[:10]

    # news category all
    news_category_all = NewsCategory.objects.all()

    # sponsored ads at slider
    onload_ads = CustomAds.onload_ads.filter().order_by('-pk')[:2]

    # sponsored ads at header/top
    ads_header = CustomAds.onheader_ads.filter().order_by('-pk').first()

    # sponsored ads at middle
    ads_middle_position = CustomAds.onmiddle_ads.filter().order_by('-pk').first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    # breaking news
    breaking_news = BreakingNews.publishedObjects.filter().first()

    # main lead news
    main_lead_news_list = News.leadmainobjects.all().order_by('-pk')[:2]

    # lead news small top
    lead_news_small_top = News.leadminor1objects.filter().order_by('-pk').first()

    # lead news small bottom
    lead_news_small_bottom = News.leadminor2objects.filter().order_by('-pk').first()

    # most recent news list
    most_recent_news_list = News.publishedObjects.all().order_by('-pk')[:8]

    # most popular/visited
    most_visited_news_list = News.publishedObjects.all().order_by('-number_of_visitor')[:10]

    # todays focus
    todays_focus = News.publishedObjects.all().order_by('-pk')[:8]


    # first three news cats
    frst_three_news_cats = NewsCategory.objects.filter()[:3]
    all_published_news_list = News.publishedObjects.all()
    frst_news_of_1st_3_category = []
    if frst_three_news_cats:
        for x in frst_three_news_cats:
            frst_news_of_1st_3_category.append(News.publishedObjects.filter(news_category=x).reverse().first())

    # rest of the news of first three news category
    rest_of_news_of_frst_3_category = []
    if frst_three_news_cats:
        for x in frst_three_news_cats:
            rest_of_news_of_frst_3_category.append(News.publishedObjects.filter(news_category=x).order_by('-pk')[1:5])

    # fourth news cat
    fourth_news_category = NewsCategory.objects.filter()[3:4]
    news_list_of_4th_cat = []
    if fourth_news_category:
        for news in News.publishedObjects.filter(news_category=fourth_news_category).order_by('-pk'):
            news_list_of_4th_cat.append(news)

    # fifth news cat
    fifth_news_category = NewsCategory.objects.filter()[4:5]
    news_list_of_5th_cat = []
    if fifth_news_category:
        for news in News.publishedObjects.filter(news_category=fifth_news_category).order_by('-pk')[:8]:
            news_list_of_5th_cat.append(news)


    # last three news cats
    last_three_news_cats = NewsCategory.objects.filter()[5:8]
    news_list_of_1st_news_of_last_3_cat = []

    if last_three_news_cats:
        for news_cat in last_three_news_cats:
            news_list_of_1st_news_of_last_3_cat.append(News.publishedObjects.filter(news_category=news_cat).order_by('-pk').first())

    rest_of_news_list_of_lst_3_cat = []
    if last_three_news_cats:
        for news_cat in last_three_news_cats:
            rest_of_news_list_of_lst_3_cat.append(News.publishedObjects.filter(news_category=news_cat).order_by('-pk')[1:5])

    # about us
    about_us = AboutUs.objects.filter().first()

    # NewsEditorNameList
    newsEditorNameList = NewsEditorNameList.objects.filter().first()


    # NewsPublisherList
    newsPublisherList = NewsPublisherList.objects.filter().first()

    # social media links
    social_media_links = SocailMediaLinks.objects.filter().first()

    context = {

        # news category
        'news_category_list': news_category_list,

        # news_category_all
        'news_category_all': news_category_all,

        # onload ads
        'onload_ads': onload_ads,

        # ads at header/top
        'ads_header': ads_header,

        # ads at middle position
        'ads_middle': ads_middle_position,

        # site logo
        'site_logo' : site_logo,

        # breaking news
        'breaking_news' : breaking_news,

        'main_lead_news_list' : main_lead_news_list,
        'lead_news_small_top' : lead_news_small_top,
        'lead_news_small_bottom' : lead_news_small_bottom,
        'most_recent_news_list' : most_recent_news_list,

        'most_visited_news_list' : most_visited_news_list,

        # todays focus
        'todays_focus' : todays_focus,

        # first three news list
        'frst_3_news_cat_list' : frst_three_news_cats,
        # news list
        'all_published_news_list' : all_published_news_list,
        'first_news_of_1st_3_category' : frst_news_of_1st_3_category,
        'rest_of_news_of_frst_3_category' : rest_of_news_of_frst_3_category,

        # news list of 4th category
        '4th_news_category' : fourth_news_category,
        'news_list_of_4th_category' : news_list_of_4th_cat,

        # news list of 5th category
        '5th_news_category' : fifth_news_category,
        'news_list_of_5th_category' : news_list_of_5th_cat,

        # last three news cats
        'last_3_news_cats' : last_three_news_cats,
        'news_list_of_1st_news_of_last_3_cat' : news_list_of_1st_news_of_last_3_cat,
        'rest_of_news_list_of_lst_3_cat' : rest_of_news_list_of_lst_3_cat,

        # about us
        'about_us' : about_us,

        # NewsEditorNameList
        'newsEditorNameList': newsEditorNameList,

        # NewsPublisherList
        'newsPublisherList': newsPublisherList,

        "social_media_links" : social_media_links,
    }

    return render(request, 'front-end/home.html', context)


# news details
def front_news_details(request, pk):
    # breaking news
    breaking_news = BreakingNews.publishedObjects.filter().first()

    # grab news by it's pk
    news = News.objects.get(pk=pk)

    # sponsored ads at slider
    onload_ads = CustomAds.onload_ads.filter().order_by('-pk')[:2]

    # sponsored ads at header/top
    ads_header = CustomAds.onheader_ads.filter().order_by('-pk').first()

    # sponsored ads at middle
    ads_middle_position = CustomAds.onmiddle_ads.filter().order_by('-pk').first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    if news:
        news.number_of_visitor = news.number_of_visitor + 1
        news.save()

    news_tags = str(news.news_tags).split(',')

    # related news of current news
    related_news = News.publishedObjects.filter(news_category=news.news_category).exclude(pk=pk).order_by('-pk')[:4]

    # most recent news list
    most_recent_news_list = News.objects.all().order_by('-pk')[:8]

    # most popular/visited
    most_visited_news_list = News.publishedObjects.all().order_by('-number_of_visitor')[:10]

    # all news categories
    news_category_list = NewsCategory.objects.filter()[:7]

    # news category all
    news_category_all = NewsCategory.objects.all()

    # about us
    about_us = AboutUs.objects.filter().first()

    # NewsEditorNameList
    newsEditorNameList = NewsEditorNameList.objects.filter().first()

    # NewsPublisherList
    newsPublisherList = NewsPublisherList.objects.filter().first()

    # social media links
    social_media_links = SocailMediaLinks.objects.filter().first()

    context = {
        'news' : news,
        'news_tags' : news_tags,
        'related_news_list' : related_news,

        # onload ads
        'onload_ads': onload_ads,

        # ads at header/top
        'ads_header': ads_header,

        # ads at middle position
        'ads_middle': ads_middle_position,

        # site logo
        'site_logo': site_logo,

        'most_recent_news_list': most_recent_news_list,

        'news_category_list' : news_category_list,
        # news_category_all
        'news_category_all': news_category_all,

        'most_visited_news_list': most_visited_news_list,

        # about us
        'about_us': about_us,

        # NewsEditorNameList
        'newsEditorNameList': newsEditorNameList,

        # NewsPublisherList
        'newsPublisherList': newsPublisherList,

        # breaking news
        'breaking_news': breaking_news,

        # social media links
        "social_media_links": social_media_links,
    }

    return render(request, 'front-end/news-details.html', context)

# news list
def front_news_list(request, pk):


    # breaking news
    breaking_news = BreakingNews.publishedObjects.filter().first()

    # grabing news category by current pk
    news_cateogory = NewsCategory.objects.get(pk=pk)

    # news category all
    news_category_all = NewsCategory.objects.all()

    # news subcategory
    news_subcats_of_current_cat = NewsSubCategory.objects.filter(news_cat=news_cateogory)

    if news_subcats_of_current_cat:

        # news category
        news_category_list = NewsCategory.objects.filter()[:10]

        # sponsored ads at slider
        onload_ads = CustomAds.onload_ads.filter().order_by('-pk')[:2]

        # sponsored ads at header/top
        ads_header = CustomAds.onheader_ads.filter().order_by('-pk').first()

        # sponsored ads at middle
        ads_middle_position = CustomAds.onmiddle_ads.filter().order_by('-pk').first()

        # logo
        site_logo = SiteLogo.objects.filter().order_by('-pk').first()

        # about us
        about_us = AboutUs.objects.filter().first()

        # NewsEditorNameList
        newsEditorNameList = NewsEditorNameList.objects.filter().first()

        # NewsPublisherList
        newsPublisherList = NewsPublisherList.objects.filter().first()

        # news list
        news_list = News.publishedObjects.all()

        # news subcats with news
        news_subcats_with_news = []
        for news in news_list:
            if news.news_subcategory in news_subcats_of_current_cat and news.news_subcategory not in news_subcats_with_news:
                news_subcats_with_news.append(news.news_subcategory)

        # news list of subcats
        news_list_of_current_subcats = []
        for subcat in news_subcats_with_news:
            news_list_of_current_subcats.append(News.publishedObjects.filter(news_subcategory=subcat).order_by('-pk')[:8])

        # most recent news of current cat
        recent_news_list = News.publishedObjects.filter(news_category=news_cateogory).order_by('-pk')[:8]

        # social media links
        social_media_links = SocailMediaLinks.objects.filter().first()

        context = {

            "social_media_links": social_media_links,

            # onload ads
            'onload_ads': onload_ads,

            # ads at header/top
            'ads_header': ads_header,

            # ads at middle position
            'ads_middle': ads_middle_position,

            # news category
            'news_category_list': news_category_list,

            # news_category_all
            'news_category_all': news_category_all,

            # site logo
            'site_logo': site_logo,

            # about us
            'about_us': about_us,

            # NewsEditorNameList
            'newsEditorNameList': newsEditorNameList,

            # NewsPublisherList
            'newsPublisherList': newsPublisherList,

            'news_category' : news_cateogory,

            'news_list' : news_list,
            'news_list_of_current_subcats' : news_list_of_current_subcats,

            'recent_news_list' : recent_news_list,
            'news_subcats_with_news' : news_subcats_with_news,
            # breaking news
            'breaking_news': breaking_news,
        }
        return render(request, 'front-end/news-list.html', context)

    else:

        # news category
        news_category_list = NewsCategory.objects.filter()[:10]

        # sponsored ads at slider
        onload_ads = CustomAds.onload_ads.filter().order_by('-pk')[:2]

        # sponsored ads at header/top
        ads_header = CustomAds.onheader_ads.filter().order_by('-pk').first()

        # sponsored ads at middle
        ads_middle_position = CustomAds.onmiddle_ads.filter().order_by('-pk').first()

        # logo
        site_logo = SiteLogo.objects.filter().order_by('-pk').first()

        # about us
        about_us = AboutUs.objects.filter().first()

        # NewsEditorNameList
        newsEditorNameList = NewsEditorNameList.objects.filter().first()

        # NewsPublisherList
        newsPublisherList = NewsPublisherList.objects.filter().first()

        news_list = News.publishedObjects.filter(news_category=news_cateogory).order_by('-pk')[:10]

        # social media links
        social_media_links = SocailMediaLinks.objects.filter().first()

        context = {
            # news category
            'news_category_list': news_category_list,

            # news_category_all
            'news_category_all': news_category_all,

            # onload ads
            'onload_ads': onload_ads,

            # ads at header/top
            'ads_header': ads_header,

            # ads at middle position
            'ads_middle': ads_middle_position,

            # site logo
            'site_logo': site_logo,

            # about us
            'about_us': about_us,

            # NewsEditorNameList
            'newsEditorNameList': newsEditorNameList,
            # NewsPublisherList
            'newsPublisherList': newsPublisherList,

            # news current cat
            'news_cateogory' : news_cateogory,
            'news_list_of_current_cat' : news_list,

            # breaking news
            'breaking_news': breaking_news,

            "social_media_links": social_media_links,
        }
        return render(request, 'front-end/news-list-single-cat.html', context)

    return render(request, 'front-end/news-list.html')


# news list of single subcategory
def front_news_list_subcat(request, pk):

    # breaking news
    breaking_news = BreakingNews.publishedObjects.filter().first()

    # grabing news category by current pk
    news_subcateogory = NewsSubCategory.objects.get(pk=pk)

    # grabing all the news
    newsListOfCurrentSubcat = News.publishedObjects.filter(news_subcategory=news_subcateogory)[:10]

    # news category all
    news_category_all = NewsCategory.objects.all()

    # news category
    news_category_list = NewsCategory.objects.filter()[:10]

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    # about us
    about_us = AboutUs.objects.filter().first()

    # NewsEditorNameList
    newsEditorNameList = NewsEditorNameList.objects.filter().first()

    # NewsPublisherList
    newsPublisherList = NewsPublisherList.objects.filter().first()

    # sponsored ads at slider
    onload_ads = CustomAds.onload_ads.filter().order_by('-pk')[:2]

    # sponsored ads at header/top
    ads_header = CustomAds.onheader_ads.filter().order_by('-pk').first()

    # sponsored ads at middle
    ads_middle_position = CustomAds.onmiddle_ads.filter().order_by('-pk').first()

    # social media links
    social_media_links = SocailMediaLinks.objects.filter().first()

    context = {

        'news_category_list': news_category_list,
        # news_category_all
        'news_category_all': news_category_all,

        # onload ads
        'onload_ads': onload_ads,

        # ads at header/top
        'ads_header': ads_header,

        # ads at middle position
        'ads_middle': ads_middle_position,

        # site logo
        'site_logo': site_logo,

        # about us
        'about_us': about_us,

        # NewsEditorNameList
        'newsEditorNameList': newsEditorNameList,

        # NewsPublisherList
        'newsPublisherList': newsPublisherList,

        # news subcat
        'news_subcateogory' : news_subcateogory,

        # news list by news subcat
        'newsListOfCurrentSubcat' : newsListOfCurrentSubcat,

        # breaking news
        'breaking_news': breaking_news,

        # social media links
        "social_media_links": social_media_links,
    }

    return render(request, 'front-end/news-list-subcat.html', context)


# search news by region
def front_searchNewsByRegion(request):

    # breaking news
    breaking_news = BreakingNews.publishedObjects.filter().first()

    # news category all
    news_category_all = NewsCategory.objects.all()

    # news category
    news_category_list = NewsCategory.objects.filter()[:10]

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    # about us
    about_us = AboutUs.objects.filter().first()

    # NewsEditorNameList
    newsEditorNameList = NewsEditorNameList.objects.filter().first()

    # NewsPublisherList
    newsPublisherList = NewsPublisherList.objects.filter().first()

    # sponsored ads at slider
    onload_ads = CustomAds.onload_ads.filter().order_by('-pk')[:2]

    # sponsored ads at header/top
    ads_header = CustomAds.onheader_ads.filter().order_by('-pk').first()

    # sponsored ads at middle
    ads_middle_position = CustomAds.onmiddle_ads.filter().order_by('-pk').first()

    # social media links
    social_media_links = SocailMediaLinks.objects.filter().first()

    if request.method == 'POST':
        division = request.POST['news-division']
        district = request.POST['news-district']
        upozilla = request.POST['news-upozilla']

        if division and district and upozilla:
            news = News.publishedObjects.filter(division_of_news=division).filter(zilla_of_news=district).filter(upozilla_of_news=upozilla)

            context = {
                'news' : news,

                # breaking news
                'breaking_news': breaking_news,

                'news_category_list': news_category_list,
                # news_category_all
                'news_category_all': news_category_all,

                # onload ads
                'onload_ads': onload_ads,

                # ads at header/top
                'ads_header': ads_header,

                # ads at middle position
                'ads_middle': ads_middle_position,

                # site logo
                'site_logo': site_logo,

                # about us
                'about_us': about_us,

                # NewsEditorNameList
                'newsEditorNameList': newsEditorNameList,

                # NewsPublisherList
                'newsPublisherList': newsPublisherList,

                # social media links
                "social_media_links": social_media_links,

            }
            return render(request, 'front-end/search-news-by-region.html', context)

    return render(request, 'front-end/search-news-by-region.html')


# contact
def front_contact(request):

    # breaking news
    breaking_news = BreakingNews.publishedObjects.filter().first()
    # news category
    news_category_list = NewsCategory.objects.filter()[:10]

    # news category all
    news_category_all = NewsCategory.objects.all()

    # site information
    contact_information = SiteContactInfo.objects.filter().first()

    # site contact information bangla
    contact_info_bd = SiteContactInfoBangla.objects.filter().first()

    # about us
    about_us = AboutUs.objects.filter().first()

    # NewsEditorNameList
    newsEditorNameList = NewsEditorNameList.objects.filter().first()

    # NewsPublisherList
    newsPublisherList = NewsPublisherList.objects.filter().first()

    # social media links
    social_media_links = SocailMediaLinks.objects.filter().first()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']

        if name and email and phone and msg:
            msg_model = Message(name=name, email=email, phone=phone, msg=msg)
            msg_model.save()
            messages.success(request, "Successfully sent your message!")
            return redirect('frontEndContact')
        else:
            messages.warning(request, "Something wrong! Try again!")
            return redirect('frontEndContact')

    context = {

        # news category
        'news_category_list': news_category_list,

        # news_category_all
        'news_category_all': news_category_all,

        # contact info
        'contact_info' : contact_information,
        'contact_info_bd' : contact_info_bd,

        # about us
        'about_us': about_us,

        # NewsEditorNameList
        'newsEditorNameList': newsEditorNameList,

        # NewsPublisherList
        'newsPublisherList': newsPublisherList,

        # breaking news
        'breaking_news': breaking_news,

        # social media links
        "social_media_links": social_media_links,
    }

    return render(request, 'front-end/contact.html', context)


# search result
def front_searhResult(request):

    # breaking news
    breaking_news = BreakingNews.publishedObjects.filter().first()
    # news category
    news_category_list = NewsCategory.objects.filter()[:10]

    # news category all
    news_category_all = NewsCategory.objects.all()

    # about us
    about_us = AboutUs.objects.filter().first()

    # NewsEditorNameList
    newsEditorNameList = NewsEditorNameList.objects.filter().first()

    # NewsPublisherList
    newsPublisherList = NewsPublisherList.objects.filter().first()

    # social media links
    social_media_links = SocailMediaLinks.objects.filter().first()


    if request.method == "POST":
        search_text = request.POST['search_post']

        if search_text:
            news_list_according_to_search = News.publishedObjects.filter(
                Q(news_title__icontains=search_text) | Q(news_details__icontains=search_text)
            ).order_by('-pk')

            context = {
                'searched_result' : news_list_according_to_search,

                # news category
                'news_category_list': news_category_list,

                # news_category_all
                'news_category_all': news_category_all,

                # about us
                'about_us': about_us,

                # NewsEditorNameList
                'newsEditorNameList': newsEditorNameList,

                # NewsPublisherList
                'newsPublisherList': newsPublisherList,

                # breaking news
                'breaking_news': breaking_news,

                # social media links
                "social_media_links": social_media_links,
            }
            return render(request, 'front-end/searched_result.html', context)

    return render(request, 'front-end/searched_result.html')



