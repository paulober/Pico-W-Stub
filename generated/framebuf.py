"""
Module: 'framebuf' on micropython-v1.20-441-rp2
"""
# MCU: {'ver': 'v1.20-441', 'build': '441', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.20.0', 'release': '1.20.0', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.5.7
from typing import Any


class FrameBuffer():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def blit(self, *args, **kwargs) -> Any:
        ...

    def ellipse(self, *args, **kwargs) -> Any:
        ...

    def fill(self, *args, **kwargs) -> Any:
        ...

    def fill_rect(self, *args, **kwargs) -> Any:
        ...

    def hline(self, *args, **kwargs) -> Any:
        ...

    def line(self, *args, **kwargs) -> Any:
        ...

    def pixel(self, *args, **kwargs) -> Any:
        ...

    def poly(self, *args, **kwargs) -> Any:
        ...

    def rect(self, *args, **kwargs) -> Any:
        ...

    def scroll(self, *args, **kwargs) -> Any:
        ...

    def text(self, *args, **kwargs) -> Any:
        ...

    def vline(self, *args, **kwargs) -> Any:
        ...

def FrameBuffer1(*args, **kwargs) -> Any:
    ...

GS2_HMSB = 5 # type: int
GS4_HMSB = 2 # type: int
GS8 = 6 # type: int
MONO_HLSB = 3 # type: int
MONO_HMSB = 4 # type: int
MONO_VLSB = 0 # type: int
MVLSB = 0 # type: int
RGB565 = 1 # type: int
