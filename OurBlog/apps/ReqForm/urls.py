#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 20:45
# @Author  : Xuegod Teacher For
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from .views import index,reqform,formTest
urlpatterns = [
    url(r'^$',reqform),
    url(r'^formtest/',formTest),

]