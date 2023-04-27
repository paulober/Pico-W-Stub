"""
Module: '_uasyncio' on micropython-v1.20-rp2
"""
# MCU: {'ver': 'v1.20', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.20.0', 'release': '1.20.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any


class Task():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TaskQueue():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def pop(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def peek(self, *args, **kwargs) -> Any:
        ...

    def push(self, *args, **kwargs) -> Any:
        ...

