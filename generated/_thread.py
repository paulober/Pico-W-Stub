"""
Module: '_thread' on micropython-v1.20-441-rp2
"""
# MCU: {'ver': 'v1.20-441', 'build': '441', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.20.0', 'release': '1.20.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any


class LockType():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def acquire(self, *args, **kwargs) -> Any:
        ...

    def locked(self, *args, **kwargs) -> Any:
        ...

    def release(self, *args, **kwargs) -> Any:
        ...

def allocate_lock(*args, **kwargs) -> Any:
    ...

def exit(*args, **kwargs) -> Any:
    ...

def get_ident(*args, **kwargs) -> Any:
    ...

def stack_size(*args, **kwargs) -> Any:
    ...

def start_new_thread(*args, **kwargs) -> Any:
    ...

