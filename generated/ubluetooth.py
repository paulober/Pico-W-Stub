"""
Module: 'ubluetooth' on micropython-v1.20-441-rp2
"""
# MCU: {'ver': 'v1.20-441', 'build': '441', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.20.0', 'release': '1.20.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any


class BLE():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def active(self, *args, **kwargs) -> Any:
        ...

    def config(self, *args, **kwargs) -> Any:
        ...

    def gap_advertise(self, *args, **kwargs) -> Any:
        ...

    def gap_connect(self, *args, **kwargs) -> Any:
        ...

    def gap_disconnect(self, *args, **kwargs) -> Any:
        ...

    def gap_scan(self, *args, **kwargs) -> Any:
        ...

    def gattc_discover_characteristics(self, *args, **kwargs) -> Any:
        ...

    def gattc_discover_descriptors(self, *args, **kwargs) -> Any:
        ...

    def gattc_discover_services(self, *args, **kwargs) -> Any:
        ...

    def gattc_exchange_mtu(self, *args, **kwargs) -> Any:
        ...

    def gattc_read(self, *args, **kwargs) -> Any:
        ...

    def gattc_write(self, *args, **kwargs) -> Any:
        ...

    def gatts_indicate(self, *args, **kwargs) -> Any:
        ...

    def gatts_notify(self, *args, **kwargs) -> Any:
        ...

    def gatts_read(self, *args, **kwargs) -> Any:
        ...

    def gatts_register_services(self, *args, **kwargs) -> Any:
        ...

    def gatts_set_buffer(self, *args, **kwargs) -> Any:
        ...

    def gatts_write(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

FLAG_INDICATE = 32 # type: int
FLAG_NOTIFY = 16 # type: int
FLAG_READ = 2 # type: int
FLAG_WRITE = 8 # type: int
FLAG_WRITE_NO_RESPONSE = 4 # type: int

class UUID():
    def __init__(self, *argv, **kwargs) -> None:
        ...

