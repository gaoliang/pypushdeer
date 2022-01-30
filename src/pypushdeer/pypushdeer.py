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

    def send_text(self, text: str, server: Optional[str] = None, pushkey: Optional[str] = None):
        if not pushkey and not self.pushkey:
            raise ValueError("pushkey must be specified")

        requests.get(server or self.server + self.endpoint, params={
            "pushkey": self.pushkey or pushkey,
            "text": text,
            "type": "text"
        })

    def send_markdown(self, text: str, server: Optional[str] = None, pushkey: Optional[str] = None):
        if not pushkey and not self.pushkey:
            raise ValueError("pushkey must be specified")

        requests.get(server or self.server + self.endpoint, params={
            "pushkey": self.pushkey or pushkey,
            "text": text,
            "type": "markdown"
        })

    def send_image(self, image_url_or_base64: str, server: Optional[str] = None, pushkey: Optional[str] = None):

        if not pushkey and not self.pushkey:
            raise ValueError("pushkey must be specified")

        requests.get(server or self.server + self.endpoint, params={
            "pushkey": self.pushkey or pushkey,
            "text": image_url_or_base64,
            "type": "image"
        })
