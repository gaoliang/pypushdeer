# pypushdeer

![](https://github.com/gaoliang/pypushdeer/actions/workflows/pytest.yml/badge.svg)
![](https://img.shields.io/pypi/wheel/pypushdeer)
![](https://img.shields.io/pypi/pyversions/pypushdeer)

[PushDeer](https://github.com/easychen/pushdeer) SDK for Python.

## install

```bash
pip install pypushdeer
```

## Usage:

### 1. Use pushdeer default server

```python3
from pypushdeer import PushDeer

pushdeer = PushDeer(pushkey="your_push_key")
pushdeer.send_text("hello world", desp="optional description")
pushdeer.send_markdown("# hello world", desp="**optional** description in markdown")
pushdeer.send_image("https://github.com/easychen/pushdeer/raw/main/doc/image/clipcode.png")
pushdeer.send_image(
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=")
```

### 2. Use self-hosted server

```python3
from pypushdeer import PushDeer

pushdeer = PushDeer(server="https://your-server-here", pushkey="your_push_key")
```

### 3. Use unique configuration for each message

```python3
from pypushdeer import PushDeer

pushdeer = PushDeer()
pushdeer.send_text("hello world", server="some_server", pushkey="some_key")
```

## TODO:

- [x] unit test
- [x] exception handling
- [ ] arguments validate