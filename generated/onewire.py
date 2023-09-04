"""
Module: 'onewire' on micropython-v1.20-441-rp2
"""
# MCU: {'ver': 'v1.20-441', 'build': '441', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.20.0', 'release': '1.20.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any


class OneWireError(Exception):
    ...

class OneWire():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def crc8(self, *args, **kwargs) -> Any:
        ...

    def readbit(self, *args, **kwargs) -> Any:
        ...

    def readbyte(self, *args, **kwargs) -> Any:
        ...

    def reset(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def writebit(self, *args, **kwargs) -> Any:
        ...

    def writebyte(self, *args, **kwargs) -> Any:
        ...

    def select_rom(self, *args, **kwargs) -> Any:
        ...

    MATCH_ROM = 85 # type: int
    SEARCH_ROM = 240 # type: int
    SKIP_ROM = 204 # type: int
