import json
from typing import Optional

import requests


class PushDeer:
    server = "https://api2.pushdeer.com"

    endpoint = "/message/push"

    pushkey = None

    result = None

    def __init__(self, server: Optional[str] = None, pushkey: Optional[str] = None):
        if server:
            self.server = server
        if pushkey:
            self.pushkey = pushkey

    def send_text(self, text: str, desp: Optional[str] = None, server: Optional[str] = None,
                  pushkey: Optional[str or list] = None):
        if not pushkey and not self.pushkey:
            raise ValueError("pushkey must be specified")
        if type(pushkey) is list:
            count = 0
            for key in pushkey:
                r = requests.get(server or self.server + self.endpoint, params={
                    "pushkey": self.pushkey or key,
                    "text": text,
                    "type": "text",
                    "desp": desp,
                })
                try:
                    self.result = json.loads(json.loads(r.text)["content"]["result"][0])
                    if self.result["success"] == 'ok':
                        count += 1
                    else:
                        pass
                except IndexError:
                    raise "pypushdeer did not receive result, send may failed"
            if count == len(pushkey):
                return True
            else:
                return False
        else:
            r = requests.get(server or self.server + self.endpoint, params={
                "pushkey": self.pushkey or pushkey,
                "text": text,
                "type": "text",
                "desp": desp,
            })
            try:
                self.result = json.loads(json.loads(r.text)["content"]["result"][0])
                if self.result["success"] == "ok":
                    return True
                else:
                    return False
            except IndexError:
                raise "pypushdeer did not receive result, send may failed"


    def send_markdown(self, text: str, desp: Optional[str] = None, server: Optional[str] = None,
                      pushkey: Optional[str] = None):
        if not pushkey and not self.pushkey:
            raise ValueError("pushkey must be specified")

        requests.get(server or self.server + self.endpoint, params={
            "pushkey": self.pushkey or pushkey,
            "text": text,
            "type": "markdown",
            "desp": desp,
        })

    def send_image(self, image_url_or_base64: str, desp: Optional[str] = None, server: Optional[str] = None,
                   pushkey: Optional[str] = None):

        if not pushkey and not self.pushkey:
            raise ValueError("pushkey must be specified")

        requests.get(server or self.server + self.endpoint, params={
            "pushkey": self.pushkey or pushkey,
            "text": image_url_or_base64,
            "type": "image",
            "desp": desp,
        })
