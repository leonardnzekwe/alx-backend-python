#!/usr/bin/env python3
"""element_length() Module"""
import typing


def element_length(
    lst: typing.Iterable[typing.Sequence],
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """element_length() function"""
    return [(i, len(i)) for i in lst]
