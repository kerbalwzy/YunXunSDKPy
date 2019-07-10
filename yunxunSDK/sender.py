# coding:utf-8
"""
实际执行各个功能的类

"""
import json

from yunxunSDK import core, mixins


class TextMessageSender(core.YunXun, mixins.TextMessageMixin):
    """
    # 发送模板短信
    # http://console.ytx.net/FileDetails
    """

    def __init__(self, appid, **kwargs):
        func = kwargs.pop("func", None) or "sms"
        func_url = kwargs.pop("func_url", None) or "TemplateSMS.wx"
        core.YunXun.__init__(self, func=func, func_url=func_url, **kwargs)
        mixins.TextMessageMixin.__init__(self, appid=appid, **kwargs)

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
