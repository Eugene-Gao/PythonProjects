# coding:utf-8

"""DjangoPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_web import views as dw_view  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', dw_view.index),  # 调用 view 中的 index()
    path('home/', dw_view.home),
    path('add/', dw_view.add, name='add'),  # 调用 view 中的 add()
    # path('add/<int:a>/<int:b>/', dw_view.old_add2_redirect),  # 调用 view 中的 add()
    path('new_add/<int:a>/<int:b>/', dw_view.add2, name='add2'), #

]