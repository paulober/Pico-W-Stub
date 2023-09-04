"""
Module: 'uasyncio.event' on micropython-v1.20-441-rp2
"""
# MCU: {'ver': 'v1.20-441', 'build': '441', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.20.0', 'release': '1.20.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any


class Event():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    wait : Any ## <class 'generator'> = <generator>
    def is_set(self, *args, **kwargs) -> Any:
        ...


class ThreadSafeFlag():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    wait : Any ## <class 'generator'> = <generator>
