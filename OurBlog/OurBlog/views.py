#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 21:12
# @Author  : Xuegod Teacher For
# @File    : views.py
# @Software: PyCharm
from django.http.response import HttpResponse,JsonResponse
#httprequest
# from django.http import HttpResponse
from django.http import HttpResponse,JsonResponse
import json

# from django.template import Context
from django.template.loader import get_template
from django.template.context import Context

def say_hello(request):
    print(request.method)
    data = {
        'name':'小马',
    }
    # 当返回的中文是乱码时，这时由于ascii码的原因，JsonResponse()在初始化的时候使用了json.dumps()把字典转换成了json格式
    # 当ensure_ascii是false的时候，可以返回ASCII码的值，否则就会被JSON转义
    # 所以含有中文的字典转json字符串时，使用json.dumps()方法要把ensure_ascii参数修改成false
    # content_type是指定MIME类型和编码，这样客户端知道主体是什么类型的资源，才能调用相应的插件或内置的程序去处理
    return JsonResponse(data,json_dumps_params={'ensure_ascii':False})
#
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
class Teacher(object):
    def teacher(self):
        return 'knowledge'

def get_page(request):
    # template = get_template('index.html')
    # context = {
    #     "name": "for",
    #     "age": 18,
    #     "project": ["python","html","linux"],
    #     "company": {"name": "xuegod", "position": "beijing"},
    #     "method": Teacher
    # }
    # return  HttpResponse(template.render(context))
    return render(request,'index.html')
News = [
    {"title": "for's editor","author": "for","time": "2018-06-13"},
    {"title": "MK's editor", "author": "MK", "time": "2018-06-13"},
    {"title": "CD's editor", "author": "CD", "time": "2018-06-13"},
    {"title": "RM's editor", "author": "RM", "time": "2018-06-13"},
    {"title": "Django's editor", "author": "Django", "time": "2018-06-13"},
    {"title": "Twisted's editor", "author": "Twisted", "time": "2018-06-13"}
]
def news(request):
    context = {
        'news':News,
        'inner':[1,2,3]
    }
    return render(request,'index.html',context=context)

Navigation = [
    {"id": 1, "label": "python", "href": "python", "parent_id": 0},
    {"id": 2, "label": "java", "href": "python", "parent_id": 0},
    {"id": 3, "label": "php", "href": "python", "parent_id": 0},
    {"id": 4, "label": ".net", "href": "python", "parent_id": 0},
    {"id": 5, "label": "django", "href": "python", "parent_id": 1},
    {"id": 6, "label": "flask", "href": "python", "parent_id": 1},
    {"id": 8, "label": "spring", "href": "python", "parent_id": 2},
    {"id": 8, "label": "xadmin", "href": "python", "parent_id": 5},
    {"id": 9, "label": "django_ckeditor", "href": "python", "parent_id": 5},
]
from django.shortcuts import render_to_response
# render
def navigation(request):
    # context = {
    #     'data':Navigation
    # }
    dat = Navigation
    return render_to_response('navigation.html',locals())