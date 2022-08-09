"""
Module: 'upip_utarfile' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any

DIRTYPE = 'dir' # type: str

class TarFile():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def next(self, *args, **kwargs) -> Any:
        ...

    def extractfile(self, *args, **kwargs) -> Any:
        ...


class FileSection():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def skip(self, *args, **kwargs) -> Any:
        ...


class TarInfo():
    def __init__(self, *argv, **kwargs) -> None:
        ...

def roundup(*args, **kwargs) -> Any:
    ...

TAR_HEADER = {} # type: dict
REGTYPE = 'file' # type: str
