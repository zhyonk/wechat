#_author_='zhyonk'
#-*- coding:utf-8 -*-
from robot import robot



if __name__ == '__main__':
    client = robot.client
    data = client.get_followers()["data"]
    print(data)

    for id in data:
        opid = data[id]
        user_info = client.get_user_info(opid,lang='zh_CN')
        headimgurl = user_info['headimgurl']
        nickname = user_info['nickname']

        print(user_info)