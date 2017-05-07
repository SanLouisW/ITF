#coding=utf-8
'''
Created on 2015年3月23日

@author: houcp
'''

import requests
import json
import jsonpointer
import jsonpatch
import traceback
from common.logutil import print_log

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#获取json值
def get_json_value(json_string, json_pointer):

    json_dict = json.loads(json_string)
    return jsonpointer.resolve_pointer(json_dict, json_pointer)


#设置json值
def set_json_value(json_string, json_pointer, json_value):

    json_dict = json.loads(json_string)
    data = jsonpatch.apply_patch(json_dict, [{
                                                   'op': 'add',
                                                   'path': json_pointer,
                                                   'value': json_value
                                                   }])

    return json.dumps(data, ensure_ascii=False)



def http_request_json(url, body="", params="", headers={},method="POST"):
    try:
        if method == "POST":
            print_log("请求url：\n"+url)
            if isinstance(body,basestring):
                body = eval(body)

            if isinstance(headers,basestring):
                headers = eval(headers)

            http_client = requests.post(url, data=body,headers=headers)
            print_log("请求消息体：\n"+json.dumps(body,ensure_ascii=False, indent=2))
            try:
                rev_msg = http_client.json()
                rev_msg = json.dumps(rev_msg, ensure_ascii=False, indent=2)
            except:

                 rev_msg = str(http_client.status_code)
            print_log("返回消息体：\n"+rev_msg)
            return rev_msg

        elif method == "GET":
            http_client = requests.get(url, params=params)
            print_log("请求url：\n"+url)
            params = json.dumps(params,ensure_ascii=False, indent=2)
            print_log("请求消息体：\n"+str(params))
            try:
                rev_msg = http_client.json()
                rev_msg = json.dumps(rev_msg, ensure_ascii=False, indent=2)
            except:
                 rev_msg = http_client.text
            print_log("返回消息体：\n"+rev_msg)
            return rev_msg

        else:
            print_log("请求方法不存在")

    except :
        traceback.print_exc()





if __name__ == "__main__":
#     url = "http://218.17.0.92:50002/supply_chain/apis/login/client_login?terminal=ios&chain_id=57f63aed19ce892079199c634ffd29a203c6523d&channel=010101&version=1.2.0.10004"
#     data = {
# 	"channel": "010101",
# 	"chain_id": "57f63aed19ce892079199c634ffd29a203c6523d",
# 	"request_data": {
# 		"password": "f4b1919d65ee53775d4edec619ec6cecb22a71bc",
# 		"account": "18312345678",
# 		"terminal": "ios",
# 		"jpush_id": "08126eca8c0"
# 	},
# 	"terminal": "ios",
# 	"version": "1.2.0.10004"
# }
    # data = set_json_value(data, "/request_data/terminal","android")
    # json_string =  http_request_json(url, data=data, method="POST")
    # print get_json_value(json_string, "/result")

    # params = {
    #    "name":"text123",
    #    "age":"25"
    # }
    #
    # http_request_json(url,params=params,method='GET')

#     url = 'http://mapp.xiaoniuapp.com/api/activity/shareRedPacket/distributeShareRedPacket'
#
#     data = {
#     "investId": "e972c5ad-e45d-4d00-9f6e-b67142f523a3",
#     "peopleUnionId": "1buTt2OO63mVZa5FwK_RIeTfrLI",
#     "userId": "",
#     "wechatName": "123",
#     "appVersion": "1.0.1",
#     "source": "wechat",
#     "token": "",
#     "wechatUrl": "http%3A%2F%2Fwx.qlogo.cn%2Fmmopen%2FT8oAXnxLbtduIJCeumbzgfJ0ClePxAWrnUjy1ydCiaKWjoGgXiaZ0M8QxKQB8E4JTzpcy3n2TWlE7CcaJ1CJTeEpviapialV5EkS%2F0"
# }
#     result = http_request_json(url,body=data)
#     id = get_json_value(result,'/data/result/id')
#
# #     url='http://mapp.xiaoniuapp.com/api/activity/shareRedPacket/countShareRedPacketForInvest.do'
# #     data ={
# #     "source": "android",
# #     "token": "4e9e6fd0-25b6-4085-b39b-949ffe684aa4",
# #     "userId": "12f45be2-cb33-4192-8434-5301574b88ba",
# #     "appVersion": "1.0.1"
# # }
# #
# #     http_request_json(url,body=data)
#
# #
#     url='http://mapp.xiaoniuapp.com/api/activity/shareRedPacket/receiveShareRedPacket'
#     data ='''{
#     "redpaperId": "8723b9314fa54c3db76ed14b72f46f54",
#     "peopleUnionId": "1buTt2OO63mVZa5FwK_RIeTfrLI",
#     "userId": "",
#     "appVersion": "1.0.1",
#     "source": "wechat",
#     "token": "",
#     "peopleMobile": "15112517941"
# }'''
#     data = set_json_value(data,'/redpaperId',id)
#     http_request_json(url,body=data)
#
#
#     url='http://mapp.xiaoniuapp.com/api/activity/shareRedPacket/queryShareRedPacketReceiveRecord'
#     data = '''{
#     "investId": "5c1deee8-2384-4328-b04b-15bc1e822595",
#     "source": "wechat",
#     "token": "",
#     "userId": "",
#     "appVersion": "1.0.1"
# }'''
#     data= set_json_value(data,'/investId', 'e972c5ad-e45d-4d00-9f6e-b67142f523a3')
#     http_request_json(url,body=data)


    url = 'http://10.10.16.239:8081/api/user/login'

    data = {
    "account": "15063011039'#",
    "regChannel": "xiaoniuapp",
    "deviceModel": "HM+1S",
    "density": "2.0",
    "loginPwd": "111111",
    "appVersion": "250",
    "source": "android",
    "systemVersion": "4.4.4",
    "t": "1458885820219",
    "resolution": "720*1280",
    "deviceToken": "a72376f73c89a33e7f2e67289fc1e6c6",
    "deviceId": "864934028914575"
}

    http_request_json(url,body=data)
