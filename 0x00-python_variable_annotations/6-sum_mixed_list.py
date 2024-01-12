#!/usr/bin/env python3
"""sum_mixed_list() Module"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """sum_mixed_list() function"""
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
