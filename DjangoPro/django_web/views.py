# coding:utf-8
from django.shortcuts import render
from django.http import *
from django.urls import reverse

# 引入我们创建的表单类
from .forms import AddForm


def index(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据
        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(u'求解结果为： ' + str(int(a) + int(b)))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})

# def index(request):
#     return render(request, 'index.html')  # 渲染模板


def home(request):
    tutorial_list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    info_list = map(str, range(100))  # 一个长度为100的 List
    param_dict = {
        'tutorial_list': tutorial_list,
        'info_dict': info_dict,
        'info_list': info_list,
    }
    return render(request, 'home.html', param_dict)   # 渲染模板


def add(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    return HttpResponse(u'求解结果为： ' + str(a+b))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse("add2: " + str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )