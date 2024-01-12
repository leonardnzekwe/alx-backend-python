#!/usr/bin/env python3
"""make_multiplier() Module"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """make_multiplier() function"""

    def multiply(number: float) -> float:
        """multiply() function"""
        return float(number * multiplier)

    return multiply
