from unittest import TestCase, mock

success = {'code': 0, 'content': {'result': ['{"counts":1,"logs":[],"success":"ok"}']}}
fail = {'code': 0, 'content': {'result': []}}


class TestPushDeer(TestCase):
    def test_send_text_success(self):
        from pypushdeer import PushDeer
        pushdeer = PushDeer()
        pushdeer.send_push_request = mock.Mock(return_value=success)
        self.assertTrue(pushdeer.send_text("text list test", pushkey=['key1', 'key2']))
        self.assertTrue(pushdeer.send_text("text test", pushkey='key'))

    def test_send_text_fail(self):
        from pypushdeer import PushDeer
        pushdeer = PushDeer()
        pushdeer.send_push_request = mock.Mock(return_value=fail)
        self.assertFalse(pushdeer.send_text("text list test", pushkey=['key1', 'key2']))
        self.assertFalse(pushdeer.send_text("text test", pushkey='key'))
        pushdeer.send_push_request = mock.Mock(return_value=success)
        with self.assertRaises(ValueError):
            pushdeer.send_text("no pushkey")
