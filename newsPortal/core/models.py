from django.db import models


class CustomAds(models.Model):

    class OnloadAds(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(ads_position="onload")

    class OnHeader(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(ads_position="on_header")

    class OnMiddle(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(ads_position="on_middle")


    ads_position = (
        ('onload', 'While Loading'),
        ('on_header', 'Top Of The Site'),
        ('on_middle', 'Middle Of The Site'),
    )

    img          = models.ImageField(upload_to='custom_ads')
    ads_position = models.CharField(max_length=255, choices=ads_position, blank=True, null=True)
    ads_url      = models.CharField(max_length=355, blank=True, null=True)
    added_at     = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # built-in objects
    objects = models.Manager()
    onload_ads = OnloadAds()
    onheader_ads = OnHeader()
    onmiddle_ads = OnMiddle()

    def __str__(self):
        return self.ads_position + '|' + str(self.pk)





