# coding:utf-8

"""
基本配置

名称	        类型	    是否必须	            描述
ACCOUNT_SID	    string	    是          云通信平台用户账户ID：对应管理控制台中的 ACCOUNT SID
AUTH_TOKEN	    string	    是          云通信平台用户账户授权令牌：对应管理控制台中的 AUTH TOKEN
VERSION	        string	    是          云通信API接口版本 目前可选版本：201512
API_HOST        string      是          云通信APT接口host 正式环境http://api.ytx.net 沙箱环境http://sandbox.ytx.net
APPS            dict        是          云通信应用表,字典键为应用名称,值为应用ID：对应控制台中的应用管理-应用列表
"""
# 以下配置信息, 取自云讯科技公司提供的接口体验

ACCOUNT_SID = '<Your Account Sid>'

AUTH_TOKEN = '<Your Auth Token>'

VERSION = '201512'

API_HOST = 'http://sandbox.ytx.net'

APPS = {
    "<Your App Name>": "<Your App Id>",
}

# 单元测试配置，如果你不需要进行单元测试，那么该项配置可以删除
# 单元测试使用标准库 unittest 编写
UNIT_TEST = {
    "template_text_message": {
        "app_name": "<Your App Name>",
        "mobile": ["<Receiver Phone 1>", "<Receiver Phone 2>"],
        "data": ["test_data1", "test_data2"],
        "template_id": 1
    },

    "template_voice_message": {
        "app_name": "<Your App Name>",
        "mobile": "<Receiver Phone 1>",
        "data": ["<Test Data 1>", "<Test Data 2>"],
        "template_id": 9
    },

    "voice_message": {
        "app_name": "<Your App Name>",
        "mobile": "<Receiver Phone 1>",
        "data": "<TestData Abc123>",
    }
}
