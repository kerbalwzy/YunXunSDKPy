# coding:utf-8
"""
功能扩展类
名称                      类型                  说明
TextMessageMixin         Class           发送普通模版短信的扩展类
"""
import json


class TemplateTextMessageMixin:
    # 发送模板短信
    # http://console.ytx.net/FileDetails

    action = "templateSms"

    def __init__(self, appid, **kwargs):
        """
        初始化
        :param appid: 应用id 用户登录云通信平台后，所创建的应用的编号appid
        :param spuid: 官方未明确说明的参数, 经过测试可以为None
        :param sppwd: 官方未明确说明的参数, 经过测试可以为None
        """
        self.appid = appid
        self.spuid = kwargs.pop("spuid", "")
        self.sppwd = kwargs.pop("sppwd", "")

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


class TemplateVoiceMessageMixin:
    # 向指定手机号码发送固定模板的语音通知
    # http://console.ytx.net/FileDetails/FileNotice

    action = "templateNoticeCall"

    def __init__(self, appid, **kwargs):
        """
        初始化
        :param appid: 应用id 用户登录云通信平台后，所创建的应用的编号appid
        """
        self.appid = appid

    def data(self, mobile, data_list, template_id, time=3, dstclid=None, speed=5):
        """
        生成发送模版语音信息的请求体数据

        :param mobile: 接收语音通知的手机号，只能是直线固话或手机，固话前要加区号
        :param data_list: 若所采用的模板中有{1}等占位符，该字符串数组的元素分别填充模板占位符
        :param template_id: 所采用的模板编号templateId
        :param time: 播放次数，默认2次，最多3次
        :param dstclid: 被叫收到的来显号码
        :param speed: 播放速度1-9，默认为5

        :return:data Bytes
        """
        data_dict = {"action": self.action,
                     "dst": mobile,
                     "appid": self.appid,
                     "templateId": template_id,
                     "datas": data_list,
                     "time": time,
                     "dstclid": dstclid,
                     "speed": speed
                     }
        data = json.dumps(data_dict)
        return data.encode()

    def send_template_voice_message(self, *args, **kwargs):
        raise NotImplementedError("`send_voice_message()` must be implemented.")


class VoiceMessageMixin:
    # 发送发送语音验证码
    # http://console.ytx.net/FileDetails/FileCodeCallOut

    action = "callOutCode"

    def __init__(self, appid, **kwargs):
        """
        初始化
        :param appid: 应用id 用户登录云通信平台后，所创建的应用的编号appid
        """
        self.appid = appid

    def data(self, mobile, data, time=3, dstclid=None):
        """
        生成向指定手机号码发送语音验证码的请求体数据。
        :param mobile: 验证码接收方的电话号码(只能是一个直线固话或手机，固话前要加区号)
        :param data: 验证码的内容(支持英文字母和数字)(长度小于20位)

        # 以下为非必传参数
        :param time: 重复播放验证码的次数，最多播放3次
        :param dstclid: 透传给被叫的号码(此功能暂未开放，目前默认为接收方的电话号码)
        :return: data Bytes
        """
        data_dict = {
            "action": self.action,
            "dst": mobile,
            "appid": self.appid,
            "code": data,
            "time": time,
            "dstclid": dstclid
        }

        data = json.dumps(data_dict)
        return data.encode()

    def send_voice_message(self, *args, **kwargs):
        raise NotImplementedError("`send_voice_code_message()` must be implemented.")


# TODO
class BidirectionalCallMixin:
    # 双向呼叫
    # http://console.ytx.net/FileDetails/FileDailBackCall
    def bidirectional_call(self, *args, **kwargs):
        raise NotImplementedError("`bidirectional_call()` must be implemented.")


# TODO
class NetworkTrafficRechargeMixin:
    # 流量充值
    # http://console.ytx.net/FileDetails/FileTrafficVII

    def network_traffic_recharge(self, *args, **kwargs):
        raise NotImplementedError("`network_traffic_recharge()` must be implemented.")

# TODO 电话会议、话单查询、余额查询
