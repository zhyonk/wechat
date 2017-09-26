#_author_='zhyonk'
#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from robot import robot
# 接收请求数据
def personal(request):
    request.encoding = 'utf-8'
    context = {}
    context['content'] = "11"
    print robot.client.grant_token()
    robot1 = robot
    return render(request, 'personal.html', context)