from django.contrib import admin
from .models import *


class NewsInfoAdmin(admin.ModelAdmin):

    list_display = ['id', 'news_title', 'news_content']


class NewsCategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'cag_name']


admin.site.register(NewsInfo, NewsInfoAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
