#_author_='zhyonk'
#-*- coding:utf-8 -*-
import urllib2
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from robot import robot
# 接收请求数据
def index(request):
    request.encoding = 'utf-8'
    context = {}
    code = request.GET['code']
    openid = getopenid(code)
    user_info = robot.client.get_user_info(openid)
    context['content']=user_info['nickname']
    print user_info
    context['headimgurl'] = user_info['headimgurl']
    return render(request, 'personal.html', context)

def getopenid(code):
    url_ = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx3fcb154832732b75&secret=6961c68cc55aad7fc460a03fb08b281c&code=" + code + "&grant_type=authorization_code"
    strHtml = urllib2.urlopen(url_).read()
    result_json = json.loads(strHtml)
    openid = result_json['openid']
    print strHtml
    return openid
