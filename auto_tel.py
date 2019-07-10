# coding=utf-8

import base64
import hashlib
import requests
import json


def get_authorization(sid, time_stamp):
    str1 = sid + '|' + time_stamp
    encodestr = base64.b64encode(str1.encode('utf-8'))
    return str(encodestr, 'utf-8')
    # return "11"


def get_sign(sid, auth_tocken, time_stamp):
    str1 = sid + auth_tocken + time_stamp
    hash = hashlib.md5()
    hash.update(str1.encode())
    return hash.hexdigest()


api_url = 'http://api.ytx.net'

accound_id = 'da5c0518f05c4f939de024e94c0adb6d'
auth_token = '8da2aede2f51498dab04e20b1702d111'
time_stamp = '20140416142030'

authorization = get_authorization(accound_id, time_stamp)
sign = get_sign(accound_id, auth_token, time_stamp)

print(authorization)
print(sign)

url = "http://api.ytx.net/201512/sid/da5c0518f05c4f939de024e94c0adb6d/call/NoticeCall.wx"

querystring = {"Sign": sign}
action = "templateNoticeCall"
dst = "13510437401"
appid = "8235c85ae38b47ebba4c52c188653c46"
dstclid = "01053189990"
templateId = "9"
# datas = [\"联想监控中心通知\",\"您的单据号为：REQ00012345\"]
datas = "[\"联想监控中心通知\",\"您的单据号为：REQ00012345\"]"

payload = "{\"action\":\"" + action + "\",\"dst\":\"" + dst + "\",\"appid\":\"" + appid + "\",\"dstclid\":\"" + dstclid + "\",\"templateId\":\"" + templateId + "\",\"datas\":" + datas + "}"

# payload = "{\"action\":\"templateNoticeCall\",\"dst\":\"13510437401\",\"appid\":\"8235c85ae38b47ebba4c52c188653c46\",\"dstclid\":\"01053189990\",\"templateId\":\"9\",\"datas\":[\"联想监控中心通知\",\"您的单据号为：REQ00012345\"]}"
headers = {
    'Content-Type': "application/json",
    'Authorization': authorization,
    'charset': "utf-8",
}

response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers, params=querystring)

print(response.text)
