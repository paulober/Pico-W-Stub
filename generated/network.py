"""
Module: 'network' on micropython-v1.20-441-rp2
"""
# MCU: {'ver': 'v1.20-441', 'build': '441', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.20.0', 'release': '1.20.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any

AP_IF = 1 # type: int
STAT_CONNECTING = 1 # type: int
STAT_CONNECT_FAIL = -1 # type: int
STAT_GOT_IP = 3 # type: int
STAT_IDLE = 0 # type: int
STAT_NO_AP_FOUND = -2 # type: int
STAT_WRONG_PASSWORD = -3 # type: int
STA_IF = 0 # type: int

class WLAN():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    PM_NONE = 16 # type: int
    PM_PERFORMANCE = 10555714 # type: int
    PM_POWERSAVE = 17 # type: int
    def active(self, *args, **kwargs) -> Any:
        ...

    def config(self, *args, **kwargs) -> Any:
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def disconnect(self, *args, **kwargs) -> Any:
        ...

    def ifconfig(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def isconnected(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def send_ethernet(self, *args, **kwargs) -> Any:
        ...

    def status(self, *args, **kwargs) -> Any:
        ...

def country(*args, **kwargs) -> Any:
    ...

def hostname(*args, **kwargs) -> Any:
    ...

def route(*args, **kwargs) -> Any:
    ...

