import json
import unittest

from yunxunSDK.sender import TemplateTextMessageSender, VoiceMessageSender
from yunxunSDK.config import APPS, UNIT_TEST


class YunXunTest(unittest.TestCase):

    def setUp(self):
        self.test_text_message_conf = UNIT_TEST["test_text_message"]
        text_message_app_id = APPS[self.test_text_message_conf["app_name"]]
        self.textMessageSender = TemplateTextMessageSender(appid=text_message_app_id)

        self.test_voice_code_message_conf = UNIT_TEST["test_voice_code_message"]
        test_voice_code_message_id = APPS[self.test_voice_code_message_conf["app_name"]]
        self.VoiceCodeMessageSender = VoiceMessageSender(appid=test_voice_code_message_id)

    def test_send_template_text_message(self):
        mobile = self.test_text_message_conf["mobile"]
        data = self.test_text_message_conf["data"]
        tid = self.test_text_message_conf["template_id"]

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
        pass

    def test_send_voice_message(self):
        mobile = self.test_voice_code_message_conf["mobile"]
        data = self.test_voice_code_message_conf["data"]

        ret = self.VoiceCodeMessageSender.send_voice_message(
            mobile=mobile,
            data=data
        )
        print("{0:*^70}".format("test_send_voice_message"))
        print(ret)
        ret.pop("requestId", "")
        target_ret = {"statusCode": "0",
                      "statusMsg": "提交成功"}

        self.assertDictEqual(ret, target_ret)
