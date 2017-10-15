from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):

    cags = NewsCategory.objects.all()

    return render(request, 'index.html', locals())


def detail(request, cag_id):

    cag = NewsCategory.objects.get(pk=cag_id)

    a = request.path()
    print(a)
    news_list = cag.newsinfo_set.all()

    return render(request, 'detail.html', locals())
