# @time: 2021/12/24 14:03
# -*- coding:utf-8 -*-
import requests
import json
import time
def test_text():

    # Webhook地址
    #url = "https://oapi.dingtalk.com/robot/send?access_token=" + " e8bXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXbfe2"
    url="https://oapi.dingtalk.com/robot/send?access_token="+"94f7f1da0e420066c0ceaca327ad7c7ff0f993d6d4b92141a8a6965dc962f690"
    print(url)
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8"
    }
    # 格式为：text
    message = "姐姐 这是深夜故事汇"
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": message + "\n"
                 "我的姐姐呀" + "\n"
                 "env" + "\n"
                 },
        "at": {
            "atMobiles": [
               19983128202 #如果需要@某人，这里写他的手机号
            ],
            "isAtAll":   ""# 如果需要@所有人，这里写1
        }
    }
    String_textMsg = json.dumps(String_textMsg)
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url, data=String_textMsg, headers=HEADERS, verify=False)
    
    print(res.text)
if __name__=="__main__":
    for i in range(20):
        test_text()

