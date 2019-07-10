# coding:utf-8

"""
核心函数与类：
名称                      类型                  说明
ytx_time_stamp          function           生成符合云讯科技格式要求的时间戳字符串
ytx_sign                function           生成公共参数Sign
ytx_authorization       function           生成公共参数Authorization
YunXun                  Class              功能基类
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
                 api_host=conf.API_HOST, **kwargs):
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
        self.func_url = func_url
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.version = version
        self.api_host = api_host

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
            funcURL=self.func_url,
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
        data = kwargs.pop('data', None)
        assert isinstance(data, bytes), "DataError, <data> must be a bytes object"

        resp = requests.request(method=kwargs.pop("method", "POST"),
                                url=kwargs.pop('url', None) or self.url,
                                data=data,
                                headers=kwargs.pop('headers', None) or self.headers,
                                **kwargs)

        return resp.json()
