"""
Module: 'uasyncio.lock' on micropython-v1.21-rp2
"""
# MCU: {'ver': 'v1.21', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.21.0', 'release': '1.21.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any


class Lock():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    acquire : Any ## <class 'generator'> = <generator>
    def locked(self, *args, **kwargs) -> Any:
        ...

    def release(self, *args, **kwargs) -> Any:
        ...

