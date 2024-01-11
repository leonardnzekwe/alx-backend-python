#!/usr/bin/env python3
"""make_multiplier() Module"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """make_multiplier() function"""

    def multiply(multiplier):
        return multiplier * multiplier

    return multiply
