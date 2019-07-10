# coding:utf-8

"""
核心函数与类：
名称                      类型                  说明
ytx_time_stamp          function           生成符合云讯科技格式要求的时间戳字符串
ytx_sign                function           生成公共参数Sign
ytx_authorization       function           生成公共参数Authorization
"""
import time
import hashlib
import base64

import requests

import yunxunSDK.config as conf


def ytx_time_stamp():
    # 生成符合云讯科技格式要求的时间戳字符串
    now = time.time()
    local_time = time.localtime(now)
    time_stamp = time.strftime("%Y%m%d%H%M%S", local_time)
    return time_stamp


def ytx_sign(account_sid=conf.ACCOUNT_SID, auth_token=conf.AUTH_TOKEN):
    """
    生成公共参数Sign

    :param account_sid: 云通信平台用户账户ID
    :param auth_token: 云通信平台用户账户授权令牌

    :return: sign String
    """
    assert isinstance(account_sid, str), "Type Error, <ACCOUNT_SID> must need be str"
    assert isinstance(auth_token, str), "Type Error, <AUTH_TOKEN> must need be str"

    raw_data = account_sid + auth_token + ytx_time_stamp()
    h = hashlib.md5()
    h.update(raw_data.encode())
    sign = h.hexdigest()
    return sign


def ytx_authorization(account_sid=conf.ACCOUNT_SID, tag="|"):
    """
    生成公共参数Authorization

    :param account_sid: 云通信平台用户账户ID
    :param tag: 分割字符

    :return: authorization String
    """
    assert isinstance(account_sid, str), "Type Error, <ACCOUNT_SID> must need be str"
    assert isinstance(tag, str), "Type Error, <tag> must need be str"

    raw_data = account_sid + tag + ytx_time_stamp()
    authorization = base64.b64encode(raw_data.encode()).decode()
    return authorization


class YunXun:

    def __init__(self, func, func_url, account_sid=conf.ACCOUNT_SID,
                 auth_token=conf.AUTH_TOKEN, version=conf.VERSION,
                 api_host=conf.API_HOST):
        """
        初始化
        :param func: 功能所属分类call【语音类】/sms【消息类】/traffic【流量类】/account【账户类】
        :param func_url: 业务功能的各类具体操作分支
        :param account_sid: 云通信平台用户账户Id, 对应管理控制台中的 ACCOUNT SID
        :param auth_token: 云通信平台用户账户授权令牌，对应管理控制台中的 AUTH TOKEN
        :param version: 云通信API接口版本,目前可选版本201512
        :param api_host: 云通信APT接口host
        """
        self.func = func
        self.funcURL = func_url
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.version = version
        self.api_host = api_host

    def send_text_message(self, *args, **kwargs):
        # 发送模板短信, http://console.ytx.net/FileDetails
        raise NotImplementedError("`send_text_message()` must be implemented.")

    def send_voice_code_message(self, *args, **kwargs):
        # 发送发送语音验证码, http://console.ytx.net/FileDetails/FileCodeCallOut
        raise NotImplementedError("`send_voice_code_message()` must be implemented.")

    def send_voice_message(self, *args, **kwargs):
        # 发送固定模板的语音通知, http://console.ytx.net/FileDetails/FileNotice
        raise NotImplementedError("`send_voice_message()` must be implemented.")

    def bidirectional_call(self, *args, **kwargs):
        # 双向呼叫, http://console.ytx.net/FileDetails/FileDailBackCall
        raise NotImplementedError("`bidirectional_call()` must be implemented.")

    def network_traffic_recharge(self, *args, **kwargs):
        # 流量充值, http://console.ytx.net/FileDetails/FileTrafficVII
        raise NotImplementedError("`network_traffic_recharge()` must be implemented.")

    # TODO 电话会议、话单查询、余额查询

    def __get_path_and_query_string(self):
        """
        返回请求路径,包含查询字符串参数
        :return: path_and_query_string String
        """
        path = "/{version}/sid/{accountSID}/{func}/{funcURL}?Sign={Sign}"
        path_and_query_string = path.format(
            version=self.version,
            accountSID=self.account_sid,
            func=self.func,
            funcURL=self.funcURL,
            Sign=ytx_sign(account_sid=self.account_sid, auth_token=self.auth_token)
        )
        return path_and_query_string

    @property
    def url(self):
        # 返回请求的完整URL
        return self.api_host + self.__get_path_and_query_string()

    @property
    def headers(self):
        # 返回请求的headers
        _headers = {
            "Accept": "application/json",
            "Content-Type": "application/json;charset=utf-8",
            "Authorization": ytx_authorization(account_sid=self.account_sid),
        }

        return _headers

    def __call__(self, **kwargs):
        """
        往云讯科技的API发起调用请求
        :param kwargs:
        :return:
        """
        data = kwargs.pop('data')
        assert isinstance(data, bytes), "DataError, <data> must be a bytes object"

        resp = requests.request(method=kwargs.pop("method", "POST"),
                                url=kwargs.pop('url') or self.url,
                                data=data,
                                headers=kwargs.pop('headers') or self.url,
                                **kwargs)

        return resp.json()
