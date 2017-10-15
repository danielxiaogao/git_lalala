from django.db import models


class NewsCategory(models.Model):

    cag_name = models.CharField(max_length=50)


class NewsInfo(models.Model):

    news_title = models.CharField(max_length=50)

    news_content = models.TextField(max_length=5000)

    news_category = models.ForeignKey('NewsCategory')
