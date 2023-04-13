from django.db import models

from account.models import User


class Location(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=20, blank=False)
    category = models.CharField(verbose_name='category', max_length=20, blank=False, default='location')
    description = models.TextField(verbose_name='description', blank=True)
    longitude = models.FloatField(verbose_name='longitude', blank=False, default=59.9594)
    latitude = models.FloatField(verbose_name='latitude', blank=False, default=30.3032)
    create_at = models.DateTimeField(auto_now_add=True)


class Url(models.Model):

    location = models.ForeignKey(Location, related_name='urls', on_delete=models.CASCADE)
    location_url = models.CharField(verbose_name='location url', max_length=200)
