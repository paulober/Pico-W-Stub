"""
Module: 'aioble.core' on micropython-v1.21-rp2
"""
# MCU: {'ver': 'v1.21', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.21.0', 'release': '1.21.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any

def stop(*args, **kwargs) -> Any:
    ...

def config(*args, **kwargs) -> Any:
    ...

def log_info(*args, **kwargs) -> Any:
    ...

def log_warn(*args, **kwargs) -> Any:
    ...

def log_error(*args, **kwargs) -> Any:
    ...


class GattError(Exception):
    ...
def ensure_active(*args, **kwargs) -> Any:
    ...

def register_irq_handler(*args, **kwargs) -> Any:
    ...

def ble_irq(*args, **kwargs) -> Any:
    ...

log_level = 1 # type: int
ble : Any ## <class 'BLE'> = <BLE>
