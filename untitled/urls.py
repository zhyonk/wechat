# -*- coding: UTF-8 -*-
"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from werobot.contrib.django import make_view
from robot import robot
from . import personal
from . import myapp
from . import checkin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# # Serializers定义了API的表现.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
# # ViewSets 定义了 视图（view） 的行为.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
#
# # Routers 提供了一种简单途径，自动地配置了URL。
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

from django.conf.urls import url, include
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# 使用自动化URL路由，转配我们的API.
# 如有额外需要, 我也为可视化API添加了登陆URLs.

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robot/', make_view(robot)),
    url(r'^index/', myapp.index),
    url(r'^personal/', personal.personal),
    url(r'^checkin/', checkin.checkin),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
