#!/usr/bin/env python3
"""sum_list() Module"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """sum_list() function"""
    sum = 0
    for i in input_list:
        sum += i
    return sum
