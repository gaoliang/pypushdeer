import json
from typing import Optional, Union
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

    def _push(self, text: str, desp: Optional[str] = None, server: Optional[str] = None,
              pushkey: Optional[str] = None, type: Optional[str] = None):

        if not pushkey and not self.pushkey:
            raise ValueError("pushkey must be specified")

        res = self._send_push_request(desp, pushkey or self.pushkey, server or self.server, text, type)
        print(res)
        if res["content"]["result"]:
            result = json.loads(res["content"]["result"][0])
            if result["success"] == "ok":
                return True
            else:
                return False
        else:
            return False

    def _send_push_request(self, desp, key, server, text, type):
        return requests.get(server + self.endpoint, params={
            "pushkey": key,
            "text": text,
            "type": type,
            "desp": desp,
        }).json()

    def send_text(self, text: str, desp: Optional[str] = None, server: Optional[str] = None,
                  pushkey: Union[str, list, None] = None):
        """
        Any text are accepted when type is text.
        @param text: message : text
        @param desp: the second part of the message (optional)
        @param server: server base
        @param pushkey: PushDeer pushkeys, multiple pushkey use list of string, single pushkey use string
        @return: Boolean
        """
        return self._push(text=text, desp=desp, server=server, pushkey=pushkey, type='text')

    def send_markdown(self, text: str, desp: Optional[str] = None, server: Optional[str] = None,
                      pushkey: Union[str, list, None] = None):
        """
        Text in Markdown format are accepted when type is markdown.
        @param text: message : text in markdown
        @param desp: the second part of the message in markdown (optional)
        @param server: optional server base
        @param pushkey: pushkey
        @return: success or not
        """
        return self._push(text=text, desp=desp, server=server, pushkey=pushkey, type='markdown')

    def send_image(self, image_src: str, desp: Optional[str] = None, server: Optional[str] = None,
                   pushkey: Union[str, list, None] = None):
        """
        Only image url are accepted by API now, when type is image.
        @param image_src: message : image URL
        @param desp: the second part of the message
        @param server: optional server http address
        @param pushkey: PushDeer pushkeys, multiple pushkey use list of string, single pushkey use string
        @return: success or not
        """
        return self._push(text=image_src, desp=desp, server=server, pushkey=pushkey, type='image')
