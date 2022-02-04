from unittest import TestCase


class TestPushDeer(TestCase):
    def test_send_text(self):
        keys = ['key1', 'key2']

        from pypushdeer import PushDeer
        pushdeer = PushDeer()
        self.assertTrue(pushdeer.send_text("hello world", pushkey=keys))
        self.assertTrue(pushdeer.send_text("hello world", pushkey=keys[0]))

    def test_send_markdown(self):
        self.fail()

    def test_send_image(self):
        self.fail()
