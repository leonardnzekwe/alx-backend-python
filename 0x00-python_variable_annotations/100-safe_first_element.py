#!/usr/bin/env python3
"""safe_first_element() Module"""
import typing


def safe_first_element(
    lst: typing.Sequence[typing.Any],
) -> typing.Union[typing.Any, None]:
    """safe_first_element() function"""
    if lst:
        return lst[0]
    else:
        return None
