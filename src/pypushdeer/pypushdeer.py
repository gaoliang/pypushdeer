import json
from typing import Optional
import requests


class PushDeer:
    server = "https://api2.pushdeer.com"
    endpoint = "/message/push"
    pushkey = None

    def __init__(self, server: Optional[str] = None, pushkey: Optional[str] = None):
        if server:
            self.server = server
        if pushkey:
            self.pushkey = pushkey

    def push(self, text: str, desp: Optional[str] = None, server: Optional[str] = None,
             pushkey: Optional[str or list] = None, text_type: Optional[str] = None):
        """
        Basic method of calling /message/push API
        @param text_type:
        @param text:
        @param desp:
        @param server:
        @param pushkey:
        @return:
        """
        if not pushkey and not self.pushkey:
            raise ValueError("pushkey must be specified")
        if type(pushkey) is list:
            count = 0
            for key in pushkey:
                r_json = self.send_push_request(desp, key, server, text, text_type)
                try:
                    result = json.loads(r_json["content"]["result"][0])
                    if result["success"] == 'ok':
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
            r_json = self.send_push_request(desp, pushkey, server, text, text_type)
            try:
                result = json.loads(r_json["content"]["result"][0])
                if result["success"] == "ok":
                    return True
                else:
                    return False
            except IndexError:
                raise "pypushdeer did not receive result, send may failed"

    def send_push_request(self, desp, key, server, text, text_type):
        return requests.get(server or self.server + self.endpoint, params={
            "pushkey": self.pushkey or key,
            "text": text,
            "type": text_type,
            "desp": desp,
        }).json()

    def send_text(self, text: str, desp: Optional[str] = None, server: Optional[str] = None,
                  pushkey: Optional[str or list] = None):
        """
        Any text are accepted when type is text.
        @param text: message : text
        @param desp: the second part of the message
        @param server: optional server http address
        @param pushkey: PushDeer pushkeys, multiple pushkey use list of string, single pushkey use string
        @return: Boolean
        """
        return self.push(text=text, desp=desp, server=server, pushkey=pushkey, text_type='text')

    def send_markdown(self, text: str, desp: Optional[str] = None, server: Optional[str] = None,
                      pushkey: Optional[str or list] = None):
        """
        Text in Markdown format are accepted when type is markdown.
        @param text: message : text in Markdown
        @param desp: the second part of the message
        @param server: optional server http address
        @param pushkey: PushDeer pushkeys, multiple pushkey use list of string, single pushkey use string
        @return: Boolean
        """
        return self.push(text=text, desp=desp, server=server, pushkey=pushkey, text_type='markdown')

    def send_image(self, image_url: str, desp: Optional[str] = None, server: Optional[str] = None,
                   pushkey: Optional[str or list] = None):
        """
        Only image url are accepted by API now, when type is image.
        @param image_url: message : image URL
        @param desp: the second part of the message
        @param server: optional server http address
        @param pushkey: PushDeer pushkeys, multiple pushkey use list of string, single pushkey use string
        @return: Boolean
        """
        return self.push(text=image_url, desp=desp, server=server, pushkey=pushkey, text_type='image')
