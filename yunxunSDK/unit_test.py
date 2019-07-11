import json
import unittest

from yunxunSDK.sender import TemplateTextMessageSender, VoiceMessageSender, TemplateVoiceMessageSender
from yunxunSDK.config import APPS, UNIT_TEST


class YunXunTest(unittest.TestCase):

    def setUp(self):
        # 创建普通模版短信的sender对象
        self.template_text_message_conf = UNIT_TEST["template_text_message"]
        text_message_app_id = APPS[self.template_text_message_conf["app_name"]]
        self.textMessageSender = TemplateTextMessageSender(appid=text_message_app_id)

        # 创建语音模版短信的sender对象
        self.template_voice_message_conf = UNIT_TEST["template_voice_message"]
        template_voice_message_id = APPS[self.template_voice_message_conf['app_name']]
        self.templateVoiceMessageSender = TemplateVoiceMessageSender(appid=template_voice_message_id)

        # 创建语音短信的sender对象
        self.voice_message_conf = UNIT_TEST["voice_message"]
        voice_message_id = APPS[self.voice_message_conf["app_name"]]
        self.VoiceMessageSender = VoiceMessageSender(appid=voice_message_id)

    def test_send_template_text_message(self):
        mobile = self.template_text_message_conf["mobile"]
        data = self.template_text_message_conf["data"]
        tid = self.template_text_message_conf["template_id"]

        ret = self.textMessageSender.send_text_message(
            mobile_list=mobile,
            data_list=data,
            template_id=tid
        )

        print("{0:*^70}".format("test_send_template_text_message"))
        print(ret)
        ret.pop("requestId", "")
        target_ret = {"statusCode": "0",
                      "statusMsg": "提交成功"}

        self.assertDictEqual(ret, target_ret)

    def test_send_template_voice_message(self):
        mobile = self.template_voice_message_conf["mobile"]
        data = self.template_voice_message_conf["data"]
        tid = self.template_voice_message_conf["template_id"]

        ret = self.templateVoiceMessageSender.send_template_voice_message(
            mobile=mobile,
            data_list=data,
            template_id=tid
        )

        print("{0:*^70}".format("test_send_template_text_message"))
        print(ret)
        ret.pop("requestId", "")
        target_ret = {"statusCode": "0",
                      "statusMsg": "提交成功"}

        self.assertDictEqual(ret, target_ret)

    def test_send_voice_message(self):
        mobile = self.voice_message_conf["mobile"]
        data = self.voice_message_conf["data"]

        ret = self.VoiceMessageSender.send_voice_message(
            mobile=mobile,
            data=data
        )
        print("{0:*^70}".format("test_send_voice_message"))
        print(ret)
        ret.pop("requestId", "")
        target_ret = {"statusCode": "0",
                      "statusMsg": "提交成功"}

        self.assertDictEqual(ret, target_ret)
