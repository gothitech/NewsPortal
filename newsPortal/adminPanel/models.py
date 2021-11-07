from django.db import models


# News Category ################################################
class NewsCategory(models.Model):
    name = models.CharField(default='', max_length=255, unique=True)
    added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + '|' + str(self.pk)

# News Subcategory ################################
class NewsSubCategory(models.Model):
    news_cat = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, null=False, blank=False)
    news_subcat = models.CharField(default='', blank=False, null=False, max_length=255)
    added_at    = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.news_subcat + '|' + str(self.pk) + '|' + str(self.news_cat)

# News manager
class BarishalNews(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division_of_news="barishal")

class ChattogramNews(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division_of_news="chattogram")

class DhakaNews(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division_of_news="dhaka")

class KhulnaNews(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division_of_news="khulna")

class RajshahiNews(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division_of_news="rajshahi")

class RangpurNews(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division_of_news="rangpur")

class MymensinghNews(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division_of_news="mymensingh")

class SylhetNews(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division_of_news="sylhet")


# Add News Model
class News(models.Model):

    news_type = (
        ('general_news', 'General News'),
        ('lead_news', 'Lead News')
    )

    lead_type = (
        ('lead_main', 'Main Lead News'),
        ('lead_minor_1', "Small Top Lead News"),
        ('lead_minor_2', 'Small Bottom Lead News')
    )

    news_division = (
        ('barishal', 'Barishal'),
        ('chattogram', 'Chattogram'),
        ('dhaka', 'Dhaka'),
        ('khulna', 'Khulna'),
        ('rajshahi', 'Rajshahi'),
        ('rangpur', 'Rangpur'),
        ('mymensingh', 'Mymensingh'),
        ('sylhet', 'Sylhet')
    )

    news_status = (
        ('publish', 'Publish'),
        ('draft', 'Draft'),
    )

    class PublishedNews(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(news_status='publish')

    class LeadMainObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(lead_types="lead_main")

    class LeadMinor1Objects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(lead_types='lead_minor_1')

    class LeadMinor2Objects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(lead_types='lead_minor_2')

    class NewsGeneralObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(news_types='general_news')

    news_types = models.CharField(default='', max_length=255, choices=news_type, blank=True, null=True)
    lead_types = models.CharField(default='', max_length=255, choices=lead_type, blank=True, null=True)

    news_status = models.CharField(default='', max_length=255, choices=news_status, blank=True, null=True)

    news_id = models.CharField(default='', max_length=255, blank=True, null=True)
    news_title = models.TextField(default='', blank=False, null=False, max_length=255)
    news_img   = models.ImageField(upload_to='news_images')
    news_img_short_description = models.CharField(default='', blank=True, null=True, max_length=255)
    news_details = models.TextField(default='', blank=False, null=False)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.PROTECT)
    news_subcategory = models.ForeignKey(NewsSubCategory, on_delete=models.PROTECT, blank=True, null=True)
    news_writer = models.CharField(max_length=255, blank=True, null=True)
    news_writer_id = models.IntegerField(default=0, blank=True, null=True)
    news_publisher = models.CharField(max_length=255, blank=True, null=True)
    news_publisher_id = models.IntegerField(default=0, blank=True, null=True)
    news_tags = models.TextField(default='', blank=True, null=True)
    number_of_visitor = models.IntegerField(default=0, blank=True, null=True)
    division_of_news = models.CharField(default='', max_length=255, choices=news_division, blank=True, null=True)
    zilla_of_news = models.CharField(default='', max_length=255, blank=True, null=True)
    upozilla_of_news = models.CharField(default='', max_length=255, blank=True, null=True)
    published_at = models.DateField(auto_now_add=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = models.Manager() # built-in manager
    leadmainobjects = LeadMainObjects() # custom manager
    leadminor1objects = LeadMinor1Objects() # custom manager
    leadminor2objects = LeadMinor2Objects() # custom manager
    newsgeneralobjects = NewsGeneralObjects() # custom manager
    publishedObjects = PublishedNews() # custom manager

    # division news manager
    barishalnewsobjects = BarishalNews()
    chattogramnewsobjects = ChattogramNews()
    dhakanewsobjects = DhakaNews()
    khulnanewsobjects = KhulnaNews()
    rajshahinewsobjects = RajshahiNews()
    rangpurnewsobjects = RangpurNews()
    mymensinghnewsobjects = MymensinghNews()
    sylhetnewsobjects= SylhetNews()

    def __str__(self):
        return self.news_title + '|' + str(self.pk)



# News gallery
class NewsGallery(models.Model):
    gallery_id = models.CharField(max_length=255, default='', blank=True, null=True)
    title = models.CharField(max_length=255, default='', blank=True, null=True)
    short_description = models.TextField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(NewsSubCategory, on_delete=models.PROTECT)

    def __str__(self):
        return self.gallery_id + '|' + str(self.pk)

class NewsImages(models.Model):
    gallery = models.ForeignKey(NewsGallery, on_delete=models.CASCADE, blank=True, null=True)
    img_id = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(blank=True, null=True, upload_to='gallery')

    def __str__(self):
        return self.img_id + '|' + str(self.pk)


# News Editor
class NewsEditorNameList(models.Model):
    name = models.CharField(default='', max_length=255, blank=False)
    added_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name + '|' + str(self.pk)

# News Publisher
class NewsPublisherList(models.Model):
    name = models.CharField(default='', max_length=255, blank=False)
    added_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name + '|' + str(self.pk)

# Breaking News
class BreakingNews(models.Model):

    class PublishedNews(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status_code=1)

    news = models.TextField(default='', max_length=255, blank=True, null=True)
    status_code = models.IntegerField(default=0, blank=True, null=True)
    added_at = models.DateField(auto_now_add=True)

    objects = models.Manager()
    publishedObjects = PublishedNews() # default manager

    def __str__(self):
        return self.news + '|' +str(self.pk)


# site logo
class SiteLogo(models.Model):
    logo = models.ImageField(upload_to="logos")
    added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.logo)

# contact information
class SiteContactInfo(models.Model):
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.email + str(self.pk)

# contact info in Bangla
class SiteContactInfoBangla(models.Model):
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.email + '|' + str(self.pk)


# about us
class AboutUs(models.Model):
    about_us = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + "|" + str(self.added_at)


# messages
class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    msg = models.TextField()

    def __str__(self):
        return self.name + "|" + self.email


# social media links
class SocailMediaLinks(models.Model):
    fb = models.CharField(max_length=255, blank=True, null=True)
    tw = models.CharField(max_length=255, blank=True, null=True)
    insgrm = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.pk)




