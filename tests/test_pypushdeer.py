from unittest import mock
import pytest
from pypushdeer import PushDeer

success_res = {'code': 0, 'content': {'result': ['{"counts":1,"logs":[],"success":"ok"}']}}
fail_res = {'code': 0, 'content': {'result': []}}


def test_send_text_success():
    pushdeer = PushDeer(pushkey="some_key")
    pushdeer._send_push_request = mock.Mock(return_value=success_res)
    assert pushdeer.send_text("text test")
    assert pushdeer.send_markdown("# text test")
    assert pushdeer.send_image("https://example.com/a.png")


def test_send_text_fail():
    pushdeer = PushDeer(pushkey="key")
    pushdeer._send_push_request = mock.Mock(return_value=fail_res)
    assert not pushdeer.send_text("text test", pushkey='key')
    assert not pushdeer.send_text("text test")
    assert not pushdeer.send_markdown("# text test")
    assert not pushdeer.send_image("https://example.com/a.png")


def test_no_push_key():
    pushdeer = PushDeer()
    pushdeer._send_push_request = mock.Mock(return_value=success_res)
    with pytest.raises(ValueError):
        pushdeer.send_text("no pushkey")
