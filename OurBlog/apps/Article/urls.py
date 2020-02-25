#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 21:10
# @Author  : Xuegod Teacher For
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from .views import *
# from Article import views
app_name = 'Article'
urlpatterns = [
    url(r'^article$',article),
    url(r'^articlelist$',articleList),
    url('^test',test,name='test'),
    url(r'^framewrok_page',framework_page)
]