# _author_='zhyonk'
# -*- coding:utf-8 -*-
from werobot import WeRoBot

robot = WeRoBot(enable_session=False,
                token='l492LBlIFo2040n04mNwFBOZ0289v90l',
                APP_ID='wx3fcb154832732b75',
                APP_SECRET='6961c68cc55aad7fc460a03fb08b281c')

client = robot.client

client.create_menu({
    "button":[
        {
            "type":"click",
            "name":"今日歌曲",
            "key":"V1001_TODAY_MUSIC"
        },
        {
            "type":"click",
            "name":"歌手简介",
            "key":"V1001_TODAY_SINGER"
        },
        {
            "name":"菜单",
            "sub_button":[
                {
                    "type":"view",
                    "name":"搜索",
                    "url":"http://www.soso.com/"
                },
                {
                    "type":"view",
                    "name":"视频",
                    "url":"http://v.qq.com/"
                },
                {
                    "type":"click",
                    "name":"赞一下我们",
                    "key":"V1001_GOOD"
                }
            ]
        }
    ]})

# print(client.get_menu())

@robot.handler
def hello(message):
    return 'Hello world'

