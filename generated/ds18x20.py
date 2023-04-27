"""
Module: 'ds18x20' on micropython-v1.20-rp2
"""
# MCU: {'ver': 'v1.20', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.20.0', 'release': '1.20.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any

def const(*args, **kwargs) -> Any:
    ...


class DS18X20():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def convert_temp(self, *args, **kwargs) -> Any:
        ...

    def read_scratch(self, *args, **kwargs) -> Any:
        ...

    def write_scratch(self, *args, **kwargs) -> Any:
        ...

    def read_temp(self, *args, **kwargs) -> Any:
        ...

