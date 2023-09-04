"""
Module: 'ussl' on micropython-v1.20-441-rp2
"""
# MCU: {'ver': 'v1.20-441', 'build': '441', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.20.0', 'release': '1.20.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any

CERT_NONE = 0 # type: int
CERT_OPTIONAL = 1 # type: int
CERT_REQUIRED = 2 # type: int
PROTOCOL_TLS_CLIENT = 0 # type: int
PROTOCOL_TLS_SERVER = 1 # type: int

class SSLContext():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def wrap_socket(self, *args, **kwargs) -> Any:
        ...

def wrap_socket(*args, **kwargs) -> Any:
    ...

