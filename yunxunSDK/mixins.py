# coding:utf-8
"""
功能扩展类
名称                      类型                  说明
TextMessageMixin         Class           发送普通模版短信的扩展类
"""
import json


class TextMessageMixin:
    # 发送模板短信
    # http://console.ytx.net/FileDetails

    action = "templateSms"

    def __init__(self, appid, **kwargs):
        """
        初始化
        :param appid: 应用id 用户登录云通信平台后，所创建的应用的编号appid
        :param spuid:
        :param sppwd:
        """
        self.appid = appid
        self.spuid = kwargs.pop("spuid", None)
        self.sppwd = kwargs.pop("sppwd", None)

    def data(self, mobile_list, data_list, template_id):
        """
        生成发送普通模版短信的请求体数据

        :param mobile_list: 手机号列表
        :param data_list: 短信内容
        :param template_id: 短信模版id

        :return:data Bytes
        """
        data_dict = {
            "appid": self.appid,
            "action": self.action,
            "mobile": ",".join(mobile_list),
            "templateId": template_id,
            "datas": data_list,
            "spuid": self.spuid,
            "sppwd": self.sppwd
        }
        data = json.dumps(data_dict)
        return data.encode()

    def send_text_message(self, *args, **kwargs):
        raise NotImplementedError("`send_text_message()` must be implemented.")


class VoiceCodeMessageMixin:
    # 发送发送语音验证码
    # http://console.ytx.net/FileDetails/FileCodeCallOut

    def send_voice_code_message(self, *args, **kwargs):
        raise NotImplementedError("`send_voice_code_message()` must be implemented.")


class VoiceMessageMixin:
    # 发送固定模板的语音通知
    # http://console.ytx.net/FileDetails/FileNotice

    def send_voice_message(self, *args, **kwargs):
        raise NotImplementedError("`send_voice_message()` must be implemented.")


class BidirectionalCallMixin:
    # 双向呼叫
    # http://console.ytx.net/FileDetails/FileDailBackCall
    def bidirectional_call(self, *args, **kwargs):
        raise NotImplementedError("`bidirectional_call()` must be implemented.")


class NetworkTrafficRechargeMixin:
    # 流量充值
    # http://console.ytx.net/FileDetails/FileTrafficVII

    def network_traffic_recharge(self, *args, **kwargs):
        raise NotImplementedError("`network_traffic_recharge()` must be implemented.")

# TODO 电话会议、话单查询、余额查询
