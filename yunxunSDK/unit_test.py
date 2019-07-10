import json
import unittest

from yunxunSDK.sender import TextMessageSender
from yunxunSDK.config import APPS, UNIT_TEST


class YunXunTest(unittest.TestCase):

    def setUp(self):
        self.test_text_message_conf = UNIT_TEST["test_text_message"]
        text_message_app_id = APPS[self.test_text_message_conf["app_name"]]
        self.textMessageSender = TextMessageSender(appid=text_message_app_id)

    def test_send_text_message(self):
        mobile = self.test_text_message_conf["mobile"]
        data = self.test_text_message_conf["data"]
        tid = self.test_text_message_conf["template_id"]

        ret = self.textMessageSender.send_text_message(
            mobile_list=mobile,
            data_list=data,
            template_id=tid
        )

        print("{0:*^70}".format("test_send_text_message"))
        print(ret)
        ret.pop("requestId")
        target_ret = {"statusCode": "0",
                      "statusMsg": "提交成功"}

        self.assertDictEqual(ret, target_ret)
