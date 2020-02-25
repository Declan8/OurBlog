#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 21:54
# @Author  : Xuegod Teacher For
# @File    : forms.py
# @Software: PyCharm
from django import forms

class UserForm(forms.Form):
    username  = forms.CharField(label='联系姓名',widget=forms.TextInput(attrs={'style':'font-size:24px'}))
    password  = forms.CharField(min_length=6,label='联系密码')
    email  = forms.CharField(max_length=32,label='联系邮箱')
    phone  = forms.CharField(min_length=11,label='联系电话')
