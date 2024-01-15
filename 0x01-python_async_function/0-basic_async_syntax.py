#!/usr/bin/env python3
"""
Module with an asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes an
    integer argument max_delay (default value: 10),
    waits for a random delay between 0 and
    max_delay (inclusive and float value) seconds,
    and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
