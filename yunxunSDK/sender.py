# coding:utf-8
"""
实际执行各个功能的类
类名                                      功能说明
TemplateTextMessageSender               发送模版文本短信
TemplateVoiceMessageSender              发送模版语音短信
VoiceMessageSender                      发送语音短信
"""
import json

from yunxunSDK.core import YunXun
from yunxunSDK.mixins import TemplateTextMessageMixin, VoiceMessageMixin, TemplateVoiceMessageMixin


class TemplateTextMessageSender(YunXun, TemplateTextMessageMixin):
    """
    # 发送模板普通文本短信
    # http://console.ytx.net/FileDetails
    """

    def __init__(self, appid, **kwargs):
        """
        :param appid: 使用的应用ID
        """
        func = kwargs.pop("func", None) or "sms"
        func_url = kwargs.pop("func_url", None) or "TemplateSMS.wx"
        YunXun.__init__(self, func=func, func_url=func_url, **kwargs)
        TemplateTextMessageMixin.__init__(self, appid=appid, **kwargs)

    def send_text_message(self, mobile_list, data_list, template_id):
        """
        :param mobile_list: 手机号列表
        :param data_list: 短信内容
        :param template_id: 短信模版id

        :return:resp_dict 发送结果
        """
        data = self.data(mobile_list, data_list, template_id)
        resp_dict = self(data=data)
        return resp_dict


class TemplateVoiceMessageSender(YunXun, TemplateVoiceMessageMixin):
    """
    # 发送发送语音验证码
    # http://console.ytx.net/FileDetails/FileCodeCallOut
    """

    def __init__(self, appid, **kwargs):
        """
        :param appid: 使用的应用ID
        """
        func = kwargs.pop("func", None) or "call"
        func_url = kwargs.pop("func_url", None) or "NoticeCall.wx"
        YunXun.__init__(self, func=func, func_url=func_url, **kwargs)
        TemplateVoiceMessageMixin.__init__(self, appid=appid, **kwargs)

    def send_template_voice_message(self, mobile, data_list, template_id, **kwargs):
        """
        发送模版语音信息
        :param mobile: 接收语音信息的手机号
        :param data_list: 模版占位数据
        :param template_id: 模版id
        :return:resp_dict 发送结果
        """
        data = self.data(mobile, data_list, template_id, **kwargs)
        resp_dict = self(data=data)
        return resp_dict


class VoiceMessageSender(YunXun, VoiceMessageMixin):
    """
    # 发送语音验证码
    # http://console.ytx.net/FileDetails/FileCodeCallOut
    """

    def __init__(self, appid, **kwargs):
        """
        :param appid: 使用的应用ID
        """
        func = kwargs.pop("func", None) or "call"
        func_url = kwargs.pop("func_url", None) or "CodeCallOut.wx"
        YunXun.__init__(self, func=func, func_url=func_url, **kwargs)
        VoiceMessageMixin.__init__(self, appid=appid, **kwargs)

    def send_voice_message(self, mobile, data, **kwargs):
        """
        :param mobile: 手机号(只能是一个直线固话或手机，固话前要加区号)
        :param data: 短信内容(支持英文字母和数字)(长度小于20位)
        :return:
        """
        assert isinstance(mobile, str), "TypeError, <mobile> must be a string"
        assert isinstance(data, str), "TypeError, <data> must be a string"
        assert data.isalnum(), "DataError, <data> can only be numbers and letters"

        data = self.data(mobile, data, **kwargs)
        resp_dict = self(data=data)
        return resp_dict
