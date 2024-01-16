#!/usr/bin/env python3
"""
Asynchronous comprehension using the async_generator coroutine.
"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers
    using an asynchronous comprehension
    over the async_generator coroutine.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]
