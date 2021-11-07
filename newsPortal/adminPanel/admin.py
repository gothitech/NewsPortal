from django.contrib import admin
from .models import *

# News Category Model
admin.site.register(NewsCategory)

# News Subcategory Model
admin.site.register(NewsSubCategory)


# News add model
admin.site.register(News)

# News Editor & Publisher
admin.site.register(NewsEditorNameList)
admin.site.register(NewsPublisherList)

# Breaking News
admin.site.register(BreakingNews)

# site logo
admin.site.register(SiteLogo)

# site contact logo
admin.site.register(SiteContactInfo)
admin.site.register(SiteContactInfoBangla)

# site gallery
admin.site.register(NewsGallery)
admin.site.register(NewsImages)

admin.site.register(AboutUs)


admin.site.register(Message)

admin.site.register(SocailMediaLinks)