import base64
from unittest import TestCase
from parametrize import parametrize


class TestPushDeer(TestCase):
    @parametrize('key', ['key1', 'key2'])
    def test_send_text(self, key):
        from pypushdeer import PushDeer
        pushdeer = PushDeer()
        # self.assertTrue(pushdeer.send_text("text list test", pushkey=key))
        self.assertTrue(pushdeer.send_text("text test", pushkey=key))

    @parametrize('key', ['key1', 'key2'])
    def test_send_markdown(self,key):
        from pypushdeer import PushDeer
        pushdeer = PushDeer()
        # self.assertTrue(pushdeer.send_markdown("# markdown list test", pushkey=key))
        self.assertTrue(pushdeer.send_markdown("# markdown test", pushkey=key))


    def test_send_image(self):
        from pypushdeer import PushDeer
        pushdeer = PushDeer()
        img = "https://www.bing.com/th?id=OHR.SpeloncatoSnow_ROW4998498676_1920x1200.jpg&rf=LaDigue_1920x1200.jpg"
        # with open("img.png","rb") as f:
        #     img = base64.b64encode(f.read())
        self.assertTrue(pushdeer.send_image(image_url=img, pushkey="key"))