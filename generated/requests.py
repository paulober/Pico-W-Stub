"""
Module: 'requests' on micropython-v1.21-rp2
"""
# MCU: {'ver': 'v1.21', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.21.0', 'release': '1.21.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any

def get(*args, **kwargs) -> Any:
    ...

def put(*args, **kwargs) -> Any:
    ...


class Response():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def json(self, *args, **kwargs) -> Any:
        ...

    text : Any ## <class 'property'> = <property>
    content : Any ## <class 'property'> = <property>
def request(*args, **kwargs) -> Any:
    ...

def head(*args, **kwargs) -> Any:
    ...

def post(*args, **kwargs) -> Any:
    ...

def patch(*args, **kwargs) -> Any:
    ...

def delete(*args, **kwargs) -> Any:
    ...

