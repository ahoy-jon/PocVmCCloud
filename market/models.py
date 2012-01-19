from django.db import models


class App(models.Model):
    '''
    Describes an app available on the market.
    '''

    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
