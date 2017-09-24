# _author_='zhyonk'
# -*- coding:utf-8 -*-

from werobot import WeRoBot

robot = WeRoBot(enable_session=False,
                token='yourtoken',
                APP_ID='l492LBlIFo2040n04mNwFBOZ0289v90l',
                APP_SECRET='d444997a9ed334f2b8c2a4cf7518d60c')


@robot.handler
def hello(message):
    return 'Hello world'
