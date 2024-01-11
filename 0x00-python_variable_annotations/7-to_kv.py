#!/usr/bin/env python3
"""to_kv() Module"""
import typing
import math


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """to_kv() function"""
    return (k, v * v)
