from django.db import models


class InstalledApp(models.Model):
    '''
    Describes app that are installed on my cloud.
    '''

    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
