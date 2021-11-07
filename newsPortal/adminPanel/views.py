from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user.models import User, UserProfile
from adminPanel.models import *
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import uuid
import re
from core.models import CustomAds




# admin panel index
@login_required(login_url='/ap/login/register')
def ap_index(request):
    # user profile
    userProfile = UserProfile.objects.get(user=request.user)

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context = {
        'userProfile': userProfile,
        'site_logo' : site_logo,
    }

    return render(request, 'back-end/admin_panel/index.html', context)

# admin panel home
@login_required(login_url='/ap/login/register')
def ap_home(request):
    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    user_list = User.objects.all()

    context = {
        'user_list' : user_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }


    return render(request, 'back-end/admin_panel/home.html', context)


# remove user
@login_required(login_url='/ap/login/register')
def ap_removeUser(request, pk):


    try:
        user = User.objects.get(pk=pk)
        user.delete()
        messages.success(request, "Successfully reoved user!")
        return redirect('apHome')
    except:
        messages.warning(request, "Can't be removed user! Try again!")
        return redirect('apHome')

    return redirect('apHome')

# admin panel add news category
@login_required(login_url='/ap/login/register')
def ap_add_news_category(request):

    if request.method == "POST":
        news_cat_name = request.POST.get('news_cat_name')

        if news_cat_name:
            news_name_capitalize = news_cat_name.capitalize()

            if len(NewsCategory.objects.filter(name=news_name_capitalize)) <= 0 :
                news_cat_model = NewsCategory(name=news_name_capitalize)
                news_cat_model.save()
                messages.success(request, "News category has been added!")
                return redirect('apAddNewsCategory')
            else:
                messages.warning(request, "This category already exist!")
                return redirect('apAddNewsCategory')

    news_cat_list = NewsCategory.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()



    context = {
        'news_cat_list': news_cat_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add_news_category.html', context)

# admin panel delete news category
@login_required(login_url='/ap/login/register')
def ap_delete_news_category(request, pk):
    try:
        news_cat = NewsCategory.objects.get(pk=pk)
        news_cat.delete()
        messages.success(request, "News category has been deleted!")
        return redirect('apAddNewsCategory')
    except:
        messages.warning(request, "Can't delte! There is something wrong!")
        return redirect('apAddNewsCategory')

    return redirect('apAddNewsCategory')

# admin panel delete news category
@login_required(login_url='/ap/login/register')
def ap_edit_news_category(request, pk):

    news_cat_model = get_object_or_404(NewsCategory, pk=pk)

    if request.method == 'POST':
        news_cat_name = request.POST.get('edit_news_cat_name')

        if news_cat_name and len(NewsCategory.objects.filter(name=news_cat_name)) <= 0:
            current_news_cat_obj = get_object_or_404(NewsCategory, pk=pk)
            current_news_cat_obj.name = news_cat_name
            current_news_cat_obj.save()
            messages.success(request, "Category name updated!")
            return redirect('apAddNewsCategory')
        else:
            messages.warning(request, "This category name alredy exists!")
            return redirect('apAddNewsCategory')

    return redirect('apAddNewsCategory')


# admin panel see all subcats by news category
@login_required(login_url='/ap/login/register')
def apNewsCats_subcategories(request, news_cat_id):

    # grab news subcat model
    news_subcat_list_by_cat_id = NewsSubCategory.objects.filter(news_cat=news_cat_id)

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'news_subcat_list_by_cat_id': news_subcat_list_by_cat_id,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/news_cats_subcat_list.html', context)


# admin panel delete subcats by news category
@login_required(login_url='/ap/login/register')
def apNewsCats_DelSubcategories(request, news_subcat_id):

    try:
        # grab news subcat model
        news_subcat_by_cat_id = NewsSubCategory.objects.get(pk=news_subcat_id)

        # grab news cat id of this current subcat
        news_cat_id = news_subcat_by_cat_id.news_cat.pk
        news_subcat_by_cat_id.delete()
        messages.success(request, "Deleted Successfully!")
        return redirect('apNewsCatsSubcatList', news_cat_id=news_cat_id)

    except:
        messages.warning(request, "There is something wrong!")
        return redirect('apAddNewsCategory')

    # return render(request, 'back-end/admin_panel/news_cats_subcat_list.html')
    return redirect('apNewsCatsSubcatList', news_cat_id=news_cat_id)


# admin panel add news sub-category
@login_required(login_url='/ap/login/register')
def ap_add_news_sub_category(request):

    news_cat_list = NewsCategory.objects.all()

    if request.method == "POST":
        news_cat_pk = request.POST.get('news_cat_name')
        news_subcat_name = request.POST.get('news_subcat_name')

        news_subcat_name_capitalize = news_subcat_name.capitalize()

        if news_cat_pk and news_subcat_name and type(int(news_cat_pk)) == int and news_cat_pk != '0':

            # grab news cat object model by news_cat_pk
            news_cat_obj = get_object_or_404(NewsCategory, pk=news_cat_pk)

            if len(NewsSubCategory.objects.filter(news_subcat=news_subcat_name_capitalize).filter(news_cat=news_cat_pk)) <= 0 :
                news_subcat_model = NewsSubCategory(news_cat=news_cat_obj, news_subcat=news_subcat_name_capitalize)
                news_subcat_model.save()
                messages.success(request, "News sub-category has been added!")
                return redirect('apAddNewsSubCat')
            else:
                messages.warning(request, "This sub-category already exist!")
                return redirect('apAddNewsSubCat')
        else:
            messages.warning(request, "Didn't select any category!")
            return redirect('apAddNewsSubCat')

    # grabing updated news subcat list
    news_updated_subcat_list = NewsSubCategory.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context = {
        'news_cat_list': news_cat_list,
        'news_updated_subcat_list': news_updated_subcat_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add_news_subCategory.html', context)


# admin panel add news sub-category
@login_required(login_url='/ap/login/register')
def apEditNewsSubcat(request, subcat_id):

    # news_cat_by_subcat_id = get_object_or_404(NewsSubCategory, pk=subcat_id)

    if request.method == "POST":
        news_cat_pk = request.POST.get('news_cat_name')
        news_subcat_name = request.POST.get('edit_news_cat_name')

        if news_cat_pk and news_subcat_name:

            # grab news cat object model by news_cat_pk
            news_cat_obj = get_object_or_404(NewsCategory, pk=news_cat_pk)

            if len(NewsSubCategory.objects.filter(news_subcat=news_subcat_name).filter(news_cat=news_cat_pk)) <= 0:
                news_subcat_model = get_object_or_404(NewsSubCategory, pk=subcat_id)
                news_subcat_model.news_cat = news_cat_obj
                news_subcat_model.news_subcat = news_subcat_name
                news_subcat_model.save()
                messages.success(request, "News sub-category has been updated!")
                return redirect('apAddNewsSubCat')
            else:
                messages.warning(request, "This sub-category already exist!")
                return redirect('apAddNewsSubCat')

    return render(request, 'back-end/admin_panel/add_news_subCategory.html')

# admin panel delete news sub-category
@login_required(login_url='/ap/login/register')
def apDelNewsSubcat(request, subcat_pk):

    try:
        news_subcat = get_object_or_404(NewsSubCategory, pk=subcat_pk)
        news_subcat.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddNewsSubCat')
    except:
        messages.success(request, "Can't be deleted! Try again!")
        return redirect('apAddNewsSubCat')

    return render(request, 'back-end/admin_panel/add_news_subCategory.html')


# admin panel add news
@login_required(login_url='/ap/login/register')
def ap_addNews(request):

    # news cat list
    news_cat_list = NewsCategory.objects.all()

    # news subcat list
    news_subcat_list = NewsSubCategory.objects.all()

    # news editor name list
    news_editorList = NewsEditorNameList.objects.all()

    # news publisher name list
    news_publisherList = NewsPublisherList.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()



    # ajax part
    # getting news category id from ajax request
    news_cat_id = request.GET.get('news_cat_id')

    if news_cat_id:
        # news_cat_by_it's id <-- got news id from ajax request -->
        selected_news_category = get_object_or_404(NewsCategory, pk=news_cat_id)

        # news subcat by cat_id
        news_subcat_list_by_cat_id = list(NewsSubCategory.objects.filter(news_cat=selected_news_category).values())
        # sending the value to ajax/js file
        if request.is_ajax():
            return JsonResponse({'news_subcat_list': news_subcat_list_by_cat_id})
    # ends ajax part


    if request.method == 'POST':
        news_title = request.POST.get('news_title')
        news_details = request.POST.get('news_details')
        news_img = request.FILES['news-img']
        news_img_short_description = request.POST.get('news_img_short_description')
        news_cat_id = request.POST.get('news_category')
        news_subcat_id = request.POST.get('news_cat_subcat')
        news_writer = request.POST.get('news_writer')
        news_publisher = request.POST.get('news_publisher')
        news_type = request.POST.get('news-type')
        lead_news_type = request.POST.get('lead-news-type')
        news_division = request.POST.get('news-division')
        news_district = request.POST.get('news-district')
        news_upozilla = request.POST.get('news-upozilla')
        news_status = request.POST.get('news_status')
        news_tags    = request.POST.get('news_tags')

        print(f'Division: {news_division}, District: {news_district}, Upozilla: {news_upozilla}')

        news_img_extension = str(news_img).split('.')
        allowed_img_extensions = ['png', 'jpg', 'jpeg', 'webp']


        if news_img_extension[len(news_img_extension)-1] in allowed_img_extensions:
            # grab news cat by news_cat_id
            news_cat = NewsCategory.objects.get(pk=news_cat_id)

            # news publisher
            publisher_name = NewsPublisherList.objects.get(pk=news_publisher).name

            # news editor/writer
            writer_name = NewsEditorNameList.objects.get(pk=news_writer).name

            # generate random news id
            random_generated_newsid = str(uuid.uuid4()).replace('-', '')[:15]

            if news_subcat_id != '':
                try:
                    # grab news-subcat by news_subcat_id
                    news_subcat = NewsSubCategory.objects.get(pk=news_subcat_id)

                    # save to news model
                    news = News(
                        news_types=news_type,
                        lead_types=lead_news_type,
                        news_id=random_generated_newsid,
                        news_title=news_title,
                        news_img=news_img,
                        news_img_short_description=news_img_short_description,
                        news_details=news_details,
                        news_category=news_cat,
                        news_subcategory=news_subcat,
                        news_writer=writer_name,
                        news_writer_id=news_writer,
                        news_publisher=publisher_name,
                        news_publisher_id=news_publisher,
                        news_tags=news_tags,
                        number_of_visitor=0,
                        division_of_news=news_division,
                        zilla_of_news=news_district,
                        upozilla_of_news=news_upozilla,
                        news_status=news_status,
                    )
                    news.save()
                    messages.success(request, "News saved successfully!")
                    return redirect('apAddNews')
                except:
                    messages.success(request, "News can't be added! Try again!")
                    return redirect('apAddNews')
            else:
                try:
                    # save to news model
                    news = News(
                        news_types=news_type,
                        lead_types=lead_news_type,
                        news_id=random_generated_newsid,
                        news_title=news_title,
                        news_img=news_img,
                        news_img_short_description=news_img_short_description,
                        news_details=news_details,
                        news_category=news_cat,
                        news_writer=writer_name,
                        news_writer_id=news_writer,
                        news_publisher=publisher_name,
                        news_publisher_id=news_publisher,
                        news_tags=news_tags,
                        number_of_visitor=0,
                        division_of_news=news_division,
                        zilla_of_news=news_district,
                        upozilla_of_news=news_upozilla,
                        news_status = news_status,
                    )
                    news.save()
                    messages.success(request, "News saved successfully!")
                    return redirect('apAddNews')
                except:
                    messages.success(request, "News can't be added! Try again!")
                    return redirect('apAddNews')

        else:
            messages.success(request, "Only [jpg, jpeg, png, webp] are allowed!")
            return redirect('apAddNews')


    context = {

        'userProfile': userProfile,

        # logo
        'site_logo': site_logo,

        # news category list
        'news_cat_list' : news_cat_list,

        # news subcategory list
        'news_subcat_list' : news_subcat_list,

        # news_editor List
        'news_editorList' : news_editorList,

        # news publisher list
        'news_publisherList' : news_publisherList,
    }

    return render(request, 'back-end/admin_panel/add-news.html', context)

# admin panel news list editor name
@login_required(login_url='/ap/login/register')
def ap_newsList(request):

    # news list
    new_list = News.objects.all().order_by('-pk')

    # ajax method starts
    news_status_request = request.GET.get('news_status')

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    if news_status_request:
        unpack_status_value = str(news_status_request).split('-')
        news_pk = unpack_status_value[len(unpack_status_value)-1]

        # news_cat_by_it's id <-- got news id from ajax request -->
        selected_news = get_object_or_404(News, pk=news_pk)
        selected_news.news_status = unpack_status_value[0]
        selected_news.save()
        messages.success(request, "News status has been updated!")
        if request.is_ajax():
            return JsonResponse({'status': "ok"})
        return redirect('apNewsList')

    # ends ajax part

    context = {
        # news list
        "news_list" : new_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }
    return render(request, "back-end/admin_panel/news-list.html", context)


# admin panel news delete
@login_required(login_url='/ap/login/register')
def ap_delNews(request, news_id):

    try:
        news = get_object_or_404(News, pk=news_id)
        fs = FileSystemStorage()
        fs.delete(news.news_img.name)
        news.delete()
        messages.success(request, "News successfully deleted!")
        return redirect('apNewsList')
    except:
        messages.warning(request, "Can't be deleted! Try again!")
        return redirect('apNewsList')


    return redirect('apNewsList')


# admin panel news edit
@login_required(login_url='/ap/login/register')
def ap_editNews(request, news_id):

    # grab news by it's id
    news_by_news_id = get_object_or_404(News, pk=news_id)

    # news cat list
    news_cat_list = NewsCategory.objects.all()

    # news subcat list
    news_subcat_list = NewsSubCategory.objects.all()

    # news editor name list
    news_editorList = NewsEditorNameList.objects.all()

    # news publisher name list
    news_publisherList = NewsPublisherList.objects.all()

    # ajax part
    # getting news category id from ajax request
    news_cat_id = request.GET.get('news_cat_id')

    if news_cat_id:
        # news_cat_by_it's id <-- got news id from ajax request -->
        selected_news_category = get_object_or_404(NewsCategory, pk=int(news_cat_id))

        # news subcat by cat_id
        news_subcat_list_by_cat_id = list(
            NewsSubCategory.objects.filter(news_cat=selected_news_category).values())
        # sending the value to ajax/js file
        if request.is_ajax():
            return JsonResponse({'news_subcat_list': news_subcat_list_by_cat_id})
    # ends ajax part

    if request.method == 'POST':
        news_title = request.POST.get('news_title')
        news_details = request.POST.get('news_details')
        news_img_short_description = request.POST.get('news_img_short_description')
        news_cat_id_edited = request.POST.get('news_category')
        news_subcat_id = request.POST.get('news_cat_subcat')
        news_writer_id = request.POST.get('news_writer')
        news_publisher_id = request.POST.get('news_publisher')
        news_tags = request.POST.get('news_tags')

        # filtered_news_title = re.compile(r'<[^>]+>').sub('', news_title)
        # filtered_news_details = re.compile(r'<[^>]+>').sub('', news_details)


        try:
            # getting news editor publisher
            news_editorModel = NewsEditorNameList.objects.get(pk=news_writer_id)
            news_publisherModel = NewsPublisherList.objects.get(pk=news_publisher_id)

            news_img = request.FILES['news-img']

            # deleting old image
            fs = FileSystemStorage()
            fs.delete(news_by_news_id.news_img.name)

            if news_subcat_id != '':
                news_by_news_id.news_img = news_img
                news_by_news_id.news_title = news_title
                news_by_news_id.news_details = news_details
                news_by_news_id.news_img_short_description = news_img_short_description
                news_by_news_id.news_category = NewsCategory.objects.get(pk=news_cat_id_edited)
                news_by_news_id.news_subcategory = NewsSubCategory.objects.get(pk=news_subcat_id)
                news_by_news_id.news_writer = news_editorModel.name
                news_by_news_id.news_writer_id = news_writer_id
                news_by_news_id.news_publisher = news_publisherModel.name
                news_by_news_id.news_publisher_id = news_publisher_id
                news_by_news_id.news_tags = news_tags
                news_by_news_id.save()
                messages.success(request, "News Successfully updated!")
                return redirect('apNewsList')
            else:
                news_by_news_id.news_img = news_img
                news_by_news_id.news_title = news_title
                news_by_news_id.news_details = news_details
                news_by_news_id.news_img_short_description = news_img_short_description
                news_by_news_id.news_category = NewsCategory.objects.get(pk=news_cat_id_edited)
                news_by_news_id.news_writer = news_editorModel.name
                news_by_news_id.news_writer_id = news_writer_id
                news_by_news_id.news_publisher = news_publisherModel.name
                news_by_news_id.news_publisher_id = news_publisher_id
                news_by_news_id.news_tags = news_tags
                news_by_news_id.save()
                messages.success(request, "News Successfully updated!")
                return redirect('apNewsList')
        except:
            if news_subcat_id != '':
                news_by_news_id.news_title = news_title
                news_by_news_id.news_details = news_details
                news_by_news_id.news_img_short_description = news_img_short_description
                news_by_news_id.news_category = NewsCategory.objects.get(pk=news_cat_id_edited)
                news_by_news_id.news_subcategory = NewsSubCategory.objects.get(pk=news_subcat_id)
                news_by_news_id.news_writer = news_editorModel.name
                news_by_news_id.news_writer_id = news_writer_id
                news_by_news_id.news_publisher = news_publisherModel.name
                news_by_news_id.news_publisher_id = news_publisher_id
                news_by_news_id.news_tags = news_tags
                news_by_news_id.save()
                messages.success(request, "News Successfully updated!")
                return redirect('apNewsList')
            else:
                news_by_news_id.news_title = news_title
                news_by_news_id.news_details = news_details
                news_by_news_id.news_img_short_description = news_img_short_description
                news_by_news_id.news_category = NewsCategory.objects.get(pk=news_cat_id_edited)
                news_by_news_id.news_writer = news_editorModel.name
                news_by_news_id.news_writer_id = news_writer_id
                news_by_news_id.news_publisher = news_publisherModel.name
                news_by_news_id.news_publisher_id = news_publisher_id
                news_by_news_id.news_tags = news_tags
                news_by_news_id.save()
                messages.success(request, "News Successfully updated!")
                return redirect('apNewsList')

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context = {
        # news by it's id
        'news_by_news_id' : news_by_news_id,

        # news category list
        'news_cat_list': news_cat_list,

        # news subcategory list
        'news_subcat_list': news_subcat_list,

        # news_editor List
        'news_editorList': news_editorList,

        # news publisher list
        'news_publisherList': news_publisherList,

        'site_logo': site_logo,
    }

    return render(request, "back-end/admin_panel/edit-news.html", context)


# admin panel add news editor name
@login_required(login_url='/ap/login/register')
def ap_addNewsEditor(request):

    # news editor model
    news_editor_list = NewsEditorNameList.objects.all()

    # news editor model
    news_publisher_list = NewsPublisherList.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    if request.method == 'POST':
        editor_name = request.POST.get('news-editor-name')
        editor_name_capitalize = editor_name.title()
        if len(NewsEditorNameList.objects.filter(name=editor_name_capitalize)) <= 0:
            news_editor_model = NewsEditorNameList(name=editor_name_capitalize)
            news_editor_model.save()
            messages.success(request, "Successfully added new Publisher!")
            return redirect('apAddNewsEditor')
        else:
            messages.warning(request, "This name already exist!")
            return redirect('apAddNewsEditor')


    context = {
        # news editor list
        'news_editor_list' : news_editor_list,

        # news editor list
        'news_publisher_list': news_publisher_list,

        # user profile
        'userProfile': userProfile,

        # logo
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add-news-editor-publisher.html', context)

# admin panel delete news editor name
@login_required(login_url='/ap/login/register')
def ap_delNewsEditor(request, pk):

    try:
        news_editor = get_object_or_404(NewsEditorNameList, pk=pk)
        news_editor.delete()
        messages.success(request, "Successfully deleted Editor name!")
        return redirect('apAddNewsEditor')
    except:
        messages.warning(request, "Can't be deleted Editor name!")
        return redirect('apAddNewsEditor')

    return redirect('apAddNewsEditor')

# admin panel edit news editor name
@login_required(login_url='/ap/login/register')
def ap_editNewsEditor(request, pk):

    if request.method == 'POST':
        editor_name = request.POST.get('edit_news_cat_name')

        if len(NewsEditorNameList.objects.filter(name=editor_name)) <= 0:
            news_editor_model = get_object_or_404(NewsEditorNameList, pk=pk)
            news_editor_model.name = editor_name
            news_editor_model.save()
            messages.success(request, "Successfully updated News Editor name!")
            return redirect('apAddNewsEditor')
        else:
            essages.warning(request, "This name already exist!")
            return redirect('apAddNewsEditor')


    return redirect('apAddNewsEditor')


# admin panel add news editor name
@login_required(login_url='/ap/login/register')
def ap_addNewsPublisher(request):


    # news editor model
    news_editor_list = NewsEditorNameList.objects.all()

    # news editor model
    news_publisher_list = NewsPublisherList.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    if request.method == 'POST':
        publisher_name = request.POST.get('publisher_name')

        capitalize_publisher_name = publisher_name.title()

        if len(NewsPublisherList.objects.filter(name=capitalize_publisher_name)) <= 0:
            news_publisher_model = NewsPublisherList(name=capitalize_publisher_name)
            news_publisher_model.save()
            messages.success(request, "Successfully added new Editor!")
            return redirect('apAddNewsPublisher')
        else:
            messages.warning(request, "This name already exist!")
            return redirect('apAddNewsPublisher')


    context = {
        # news editor list
        'news_editor_list': news_editor_list,

        # news editor list
        'news_publisher_list' : news_publisher_list,

        # user profile
        'userProfile': userProfile,

        # logo
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add-news-editor-publisher.html', context)


# admin panel delete news publisher name
@login_required(login_url='/ap/login/register')
def ap_delNewsPublisher(request, pk):

    try:
        news_publisher = get_object_or_404(NewsPublisherList, pk=pk)
        news_publisher.delete()
        messages.success(request, "Successfully deleted Publisher name!")
        return redirect('apAddNewsEditor')
    except:
        messages.warning(request, "Can't be deleted publisher name!")
        return redirect('apAddNewsEditor')

    return redirect('apAddNewsEditor')

# admin panel edit news publisher name
@login_required(login_url='/ap/login/register')
def ap_editNewsPublisher(request, pk):

    if request.method == 'POST':
        publisher_name = request.POST.get('edit_news_publisher_name')

        if len(NewsPublisherList.objects.filter(name=publisher_name)) <= 0:
            news_pubName_model = get_object_or_404(NewsPublisherList, pk=pk)
            news_pubName_model.name = publisher_name
            news_pubName_model.save()
            messages.success(request, "Successfully updated News Editor name!")
            return redirect('apAddNewsEditor')
        else:
            essages.warning(request, "This name already exist!")
            return redirect('apAddNewsEditor')


    return redirect('apAddNewsEditor')


# admin panel add breaking news
@login_required(login_url='/ap/login/register')
def ap_addBreakingNews(request):

    news_status = request.GET.get('news_status')

    if news_status:
        # unpacking status value
        unpack_status_value = str(news_status).split('-')

        news_status_val = unpack_status_value[0]
        news_id = unpack_status_value[1]

        if news_status_val == "1":
            for news in BreakingNews.objects.all().exclude(pk=news_id):
                news.status_code = 0
                news.save()

            # grabing breaking news by it's id
            breaking_news = get_object_or_404(BreakingNews, pk=int(news_id))
            breaking_news.status_code = news_status_val
            breaking_news.save()
            return redirect('apAddBreakingNews')
        if news_status_val == '0':
            # grabing breaking news by it's id
            breaking_news = get_object_or_404(BreakingNews, pk=int(news_id))
            breaking_news.status_code = news_status_val
            breaking_news.save()
            return redirect('apAddBreakingNews')

        # sending the value to ajax/js file
        if request.is_ajax():
            return JsonResponse({'news_status_value': news_status_val, 'news_id': news_id})


    if request.method == 'POST':
        news_txt = request.POST.get('breaking_news_txt')

        if news_txt:
            breaking_news_model = BreakingNews(news=news_txt)
            breaking_news_model.save()
            messages.success(request, "Added successfully!")
            return redirect('apAddBreakingNews')
        else:
            messages.warning(request, "Can't be added! Pleae try again!")
            return redirect('apAddBreakingNews')

    # breaking news list
    breaking_news_list = BreakingNews.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'breaking_news_list' : breaking_news_list,

        # user profile
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add-breaking-news.html', context)

# admin panel add breaking news
@login_required(login_url='/ap/login/register')
def ap_delBreakingNews(request, news_id):

    try:
        breaking_news = get_object_or_404(BreakingNews, pk=news_id)
        breaking_news.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddBreakingNews')
    except:
        messages.warning(request, "Can't be deleted!")
        return redirect('apAddBreakingNews')
    return redirect('apAddBreakingNews')

# admin panel edit breaking news
@login_required(login_url='/ap/login/register')
def ap_editBreakingNews(request, news_id):

    if request.method == 'POST':
        news_txt = request.POST.get('breaking_news_txt')

        if news_txt:
            breaking_news_by_news_id = get_object_or_404(BreakingNews, pk=news_id)
            breaking_news_by_news_id.news = news_txt
            breaking_news_by_news_id.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAddBreakingNews')
        else:
            messages.warning(request, "Can't be updated! Please try again!")
            return redirect('apAddBreakingNews')

    return redirect('apAddBreakingNews')


# admin panel edit breaking news
@login_required(login_url='/ap/login/register')
def ap_addSiteLogo(request):

    if request.method == 'POST':

        logo = request.FILES['upload_logo']

        list_of_logo_extension = str(logo).split('.')
        allowed_logo_extensions = ['png', 'jpg', 'jpeg', 'webp']

        if list_of_logo_extension[len(list_of_logo_extension)-1] in allowed_logo_extensions:
            site_logo_model = SiteLogo(logo=logo)
            site_logo_model.save()
            messages.success(request, "Successfully uploaded!")
            return redirect('apAddSiteLogo')
        else:
            messages.warning(request, "Can't be uploaded logo! Please tyr again!")
            return redirect('apAddSiteLogo')

    # grab all logos
    logo_list = SiteLogo.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()
    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'logo_list': logo_list,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }



    return render(request, 'back-end/admin_panel/add-logo.html', context)


# admin panel delete breaking news
@login_required(login_url='/ap/login/register')
def ap_delSiteLogo(request, logo_id):

    try:
        logo_by_its_id = get_object_or_404(SiteLogo, pk=logo_id)
        fs = FileSystemStorage()
        fs.delete(logo_by_its_id.logo.name)
        logo_by_its_id.delete()
        messages.success(request, "Successfully deleted!")
        return redirect("apAddSiteLogo")
    except:
        messages.warning(request, "Can't deleted! Please try again!")
        return redirect("apAddSiteLogo")

    return redirect('apAddSiteLogo')

# admin panel delete breaking news
@login_required(login_url='/ap/login/register')
def ap_editSiteLogo(request, logo_id):

    if request.method == 'POST':
        logo = request.FILES['edit_site_logo']
        list_of_logo_extension = str(logo).split('.')
        allowed_logo_extensions = ['png', 'jpg', 'jpeg', 'webp']

        if list_of_logo_extension[len(list_of_logo_extension) - 1] in allowed_logo_extensions:
            try:
                site_logo_model = get_object_or_404(SiteLogo, pk=logo_id)
                fs = FileSystemStorage()
                fs.delete(site_logo_model.logo.name)
                site_logo_model.logo = logo
                site_logo_model.save()
                messages.success(request, "Site logo updated successfully!")
                return redirect('apAddSiteLogo')
            except:
                messages.warning(request, "Site logo can't update! Please try again!")
                return redirect('apAddSiteLogo')
        else:
            messages.warning(request, "Logo can't be updated! Please try again!")
            return redirect('apAddSiteLogo')

    return redirect('apAddSiteLogo')

# admin panel contact information
@login_required(login_url='/ap/login/register')
def ap_addSiteContactInfo(request):

    if request.method == "POST":

        phone_number = request.POST.get("mobile_no")
        email = request.POST.get("email")
        address = request.POST.get("address")

        try:
            siteContactInfor = SiteContactInfo(phone=phone_number, email=email, address=address)
            siteContactInfor.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddSiteContactInfo')
        except:
            messages.warning(request, "Can't be added! Try again!")
            return redirect('apAddSiteContactInfo')

    # site contact info
    siteContactInforList = SiteContactInfo.objects.all()

    # site contact info in bangla
    siteContactInforListBangla = SiteContactInfoBangla.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'siteContactInforList' : siteContactInforList,
        'siteContactInforListBangla': siteContactInforListBangla,
        # user profile

        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/contact_information.html', context)


# admin panel delete contact information
@login_required(login_url='/ap/login/register')
def ap_delSiteContactInfo(request, contact_id):

    try:
        siteContactInfo_by_id = get_object_or_404(SiteContactInfo, pk=contact_id)
        siteContactInfo_by_id.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddSiteContactInfo')
    except:
        messages.warning(request, "Can't be deleted! Try again!")
        return redirect('apAddSiteContactInfo')

    return redirect('apAddSiteContactInfo')

# admin panel edit contact information
@login_required(login_url='/ap/login/register')
def ap_editSiteContactInfo(request, contact_id):

    if request.method == 'POST':
        phone = request.POST.get('edit_phone')
        email = request.POST.get('edit_email')
        address = request.POST.get('edit_address')

        try:
            siteContactInfo_by_id = get_object_or_404(SiteContactInfo, pk=contact_id)
            siteContactInfo_by_id.phone = phone
            siteContactInfo_by_id.email = email
            siteContactInfo_by_id.address = address
            siteContactInfo_by_id.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAddSiteContactInfo')
        except:
            messages.warning(request, "Can't be updated! Try again!")
            return redirect('apAddSiteContactInfo')

    return redirect('apAddSiteContactInfo')


# admin panel contact information in bangla
@login_required(login_url='/ap/login/register')
def ap_addSiteContactInfoBangla(request):

    if request.method == "POST":

        phone_number = request.POST.get("mobile_no")
        email = request.POST.get("email")
        address = request.POST.get("address")

        try:
            siteContactInforBangla = SiteContactInfoBangla(phone=phone_number, email=email, address=address)
            siteContactInforBangla.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddSiteContactInfo')
        except:
            messages.warning(request, "Can't be added! Try again!")
            return redirect('apAddSiteContactInfo')

    # site contact info
    siteContactInforListBangla = SiteContactInfoBangla.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'siteContactInforListBangla' : siteContactInforListBangla,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/contact_information.html', context)

# delete site contact info bangla
@login_required(login_url='/ap/login/register')
def ap_deleteSiteContactInfoBangla(request, pk):

    try:
        site_contact_info_bd = SiteContactInfoBangla.objects.get(pk=pk)
        site_contact_info_bd.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddSiteContactInfo')
    except:
        messages.warning(request, "Can't be deleted! Try again!")
        return redirect('apAddSiteContactInfo')

    return redirect('apAddSiteContactInfo')


# delete site contact info bangla
@login_required(login_url='/ap/login/register')
def ap_editSiteContactInfoBangla(request, pk):

    if request.method == "POST":
        phone = request.POST['edit_phone']
        email = request.POST['edit_email']
        address = request.POST['edit_address']

        if phone and email and address:
            siteContactInfoBd = SiteContactInfoBangla.objects.get(pk=pk)
            siteContactInfoBd.phone = phone
            siteContactInfoBd.email = email
            siteContactInfoBd.address = address
            siteContactInfoBd.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAddSiteContactInfo')

    return redirect('apAddSiteContactInfo')

# news gallery
@login_required(login_url='/ap/login/register')
def ap_newsGallery(request):

    # news cat list
    news_cat_list = NewsCategory.objects.all()

    # news subcat list
    news_subcat_list = NewsSubCategory.objects.all()

    # ajax part
    # getting news category id from ajax request
    news_cat_id = request.GET.get('news_cat_id')

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    if news_cat_id:
        # news_cat_by_it's id <-- got news id from ajax request -->
        selected_news_category = get_object_or_404(NewsCategory, pk=int(news_cat_id))

        # news subcat by cat_id
        news_subcat_list_by_cat_id = list(
            NewsSubCategory.objects.filter(news_cat=selected_news_category).values())
        # sending the value to ajax/js file
        if request.is_ajax():
            return JsonResponse({'news_subcat_list': news_subcat_list_by_cat_id})
    # ends ajax part

    if request.method == 'POST':
        imges = request.FILES.getlist('news-img')
        img_title = request.POST.get('news_title')
        img_description = request.POST.get('news_img_short_description')
        img_cat_id = request.POST.get('news_category')
        img_subcat_id = request.POST.get('news_cat_subcat')

        gallery_id = str(uuid.uuid4()).replace('-', '2')[:10]

        if imges and img_title:

            category_name = get_object_or_404(NewsCategory, pk=img_cat_id)
            subcat_name   = get_object_or_404(NewsSubCategory, pk=img_subcat_id)

            newsGallery = NewsGallery(gallery_id=gallery_id, title=img_title, short_description=img_description, category=category_name, subcategory=subcat_name)
            newsGallery.save()

            for x in imges:
                gallery_imgs = NewsImages(gallery=newsGallery, img_id=gallery_id, img=x)
                gallery_imgs.save()

            messages.success(request, "saved successfully!")
            return redirect('apNewsGallery')

    context = {
        # news category list
        'news_cat_list': news_cat_list,

        # news subcategory list
        'news_subcat_list': news_subcat_list,

        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add-img-to-news-gallery.html', context)

# news gallery list
@login_required(login_url='/ap/login/register')
def ap_news_GalleryList(request):

    # gallery list

    galleryList = NewsGallery.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'gallery_list' : galleryList,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, "back-end/admin_panel/gallery-list.html", context)

# news gallery images
@login_required(login_url='/ap/login/register')
def ap_news_GalleryImages(request, gallery_id):

    # gallery images by id
    gallery_imges = NewsImages.objects.filter(img_id=gallery_id)

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'gallery_img' : gallery_imges,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, "back-end/admin_panel/gallery-images.html", context)


# delete galley images
@login_required(login_url='/ap/login/register')
def ap_deleteNewsGallery(request, gallery_id):

    try:
        fs = FileSystemStorage()

        gallery = get_object_or_404(NewsGallery, gallery_id=gallery_id)
        # deleting previous images
        gallery_imges = NewsImages.objects.filter(img_id=gallery_id)
        for img in gallery_imges:
            fs.delete(img.img.name)

        gallery.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apNewsGalleryList')
    except:
        messages.warning(request, "Something wrong! Please try again!")
        return redirect('apNewsGalleryList')


    return redirect('apNewsGalleryList')

# custom ads
@login_required(login_url='/ap/login/register')
def ap_addCustomAds(request):

    if request.method == 'POST':
        img = request.FILES['ads_img']
        ads_position = request.POST.get("ads_position")
        url  = request.POST.get('url')

        list_of_img_extension = str(img).split('.')
        allowed_logo_extensions = ['png', 'jpg', 'jpeg', 'webp']

        if list_of_img_extension[len(list_of_img_extension) - 1] in allowed_logo_extensions:
            if url:
                custom_ads_model = CustomAds(img=img, ads_position=ads_position, ads_url=url)
                custom_ads_model.save()
                messages.success(request, "Successfully added!")
                return redirect('apAddCustomAds')
            else:
                custom_ads_model = CustomAds(img=img, ads_position=ads_position)
                custom_ads_model.save()
                messages.success(request, "Successfully added!")
                return redirect('apAddCustomAds')
        else:
            messages.warning(request, "Can't be added! Try again!")
            return redirect('apAddCustomAds')

    # added ads list
    customAdsList = CustomAds.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'customAdsList' : customAdsList,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add-custom-ads.html', context)

# delete custom ads
@login_required(login_url='/ap/login/register')
def ap_deleteCustomAds(request, ads_id):

    try:
        fs = FileSystemStorage()
        custom_ads_model = CustomAds.objects.get(pk=ads_id)
        fs.delete(custom_ads_model.img.name)
        custom_ads_model.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddCustomAds')
    except:
        messages.warning(request, "Can't be deleted!")
        return redirect('apAddCustomAds')

    return redirect('apAddCustomAds')

# about us
@login_required(login_url='/ap/login/register')
def ap_aboutUs(request):

    if request.method == 'POST':
        about_us_txt = request.POST['about_us']

        if about_us_txt:
            about_us_model = AboutUs(about_us=about_us_txt)
            about_us_model.save()
            messages.success(request, "Successfully added!")
            return redirect('apAboutUs')
        else:
            messages.warning(request, "Can't be added! Try again!")
            return redirect('apAboutUs')

    # about us model
    aboutUs = AboutUs.objects.filter().first()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'about_us' : aboutUs,
        # user profile
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/about_us.html', context)

# delete about us
@login_required(login_url='/apLoginRegister/')
def ap_delAboutUs(request, pk):

    try:
        about_us_model = AboutUs.objects.get(pk=pk)
        about_us_model.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAboutUs')
    except:
        messages.warning(request, "Try again!")
        return redirect('apAboutUs')

    return redirect('apAboutUs')

# edit about us
@login_required(login_url='/ap/login/register')
def ap_editAboutUs(request, pk):

    if request.method == 'POST':
        about_us = request.POST['about_us']

        if about_us:
            about_us_model_byPK = AboutUs.objects.get(pk=pk)
            about_us_model_byPK.about_us = about_us
            about_us_model_byPK.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAboutUs')
        else:
            messages.warning(request, "Try again!")
            return redirect('apAboutUs')

    return redirect('apAboutUs')

# msg list
@login_required(login_url='/ap/login/register')
def ap_VisitorMsgList(request):

    # msg model
    msg_list = Message.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'msg_list' : msg_list,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, "back-end/admin_panel/msg_list.html", context)

# msg delete
@login_required(login_url='/ap/login/register')
def ap_DelVisitorMsg(request, pk):

    try:
        msg = Message.objects.get(pk=pk)
        msg.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apVisitorMessageList')
    except:
        messages.warning(request, "Something wrong! Try again!")
        return redirect('apVisitorMessageList')

    return redirect('apVisitorMessageList')


# add social media link
@login_required(login_url='/ap/login/register')
def ap_addSocialMediaLink(request):

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    if request.method == 'POST':
        fb = request.POST['fb_link']
        tw = request.POST['tw_link']
        insta = request.POST['insta_link']
        linkedIn = request.POST['linkIn_link']

        if fb != '' or tw != '' or insta != '' or linkedIn != '':
            socialMediaLink_model = SocailMediaLinks(fb=fb, tw=tw, insgrm=insta,linkedin=linkedIn)
            socialMediaLink_model.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddSocialMediaLink')

        else:
            messages.warning(request, "Something wrong! Try again!")
            return redirect('apAddSocialMediaLink')

    existing_links = SocailMediaLinks.objects.filter().first()

    context = {
        'social_media_links' : existing_links,

        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }


    return render(request, 'back-end/admin_panel/add_social_media_link.html', context)


# delete social media link
@login_required(login_url='/ap/login/register')
def ap_delSocialMediaLink(request, pk):

    try:
        social_media_link_model = SocailMediaLinks.objects.get(pk=pk)
        social_media_link_model.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddSocialMediaLink')
    except:
        messages.warning(request, "Can't be deleted! Try again!")
        return redirect('apAddSocialMediaLink')

    return redirect('apAddSocialMediaLink')


# edit social media link
@login_required(login_url='/ap/login/register')
def ap_editSocialMediaLink(request, pk):

    if request.method == 'POST':
        fb_link = request.POST['fb_link']
        tw_link = request.POST['tw_link']
        insta_link = request.POST['insta_link']
        linkIn_link = request.POST['linkIn_link']

        if fb_link != '' or tw_link != '' or insta_link != '' or linkIn_link != '':
            social_media_model = SocailMediaLinks.objects.get(pk=pk)
            social_media_model.fb = fb_link
            social_media_model.tw = tw_link
            social_media_model.insgrm = insta_link
            social_media_model.linkedin = linkIn_link

            social_media_model.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAddSocialMediaLink')
        else:
            messages.warning(request, "Can't be updated! Try again!")
            return redirect('apAddSocialMediaLink')


    return redirect('apAddSocialMediaLink')













