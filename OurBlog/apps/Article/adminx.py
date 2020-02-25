#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 20:54
# @Author  : Xuegod Teacher For
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from .models import Author,Article,Classify,Example

class AuthorAdmin(object):
    list_display = ['name','age','gender','email','phone']
    search_fields = ['name','age','gender','email','phone']
    list_filter = ['name','age','gender','email','phone']

class ExampleAdmin(object):
    list_display = ['name','type']
    search_fields = ['name','type']
    list_filter = ['name','type']

class ArticleAdmin(object):
    list_display = ['title','time','description','content','author','classify']
    search_fields = ['title','time','description','content','author','classify']
    list_filter = ['title','time','description','content','author','classify']

class ClassifyAdmin(object):
    list_display = ['label','description']
    search_fields = ['label','description']
    list_filter = ['label','description']

# xadmin.site.register(Example,ExampleAdmin)
xadmin.site.register(Author,AuthorAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Classify,ClassifyAdmin)

from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView,BaseSetting)


class GlobalSettings(object):
    # 修改title
    site_title = 'FOR后台管理界面'
    # 修改footer
    site_footer = 'FOR的公司'
    # 收起菜单
    menu_style = 'accordion'
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)








