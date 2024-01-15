#!/usr/bin/env python3
"""
Module with a function to measure the
total execution time for wait_n(n, max_delay).
"""

import time
import asyncio
from typing import List

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time
    for wait_n(n, max_delay) and return total_time / n.
    """
    start_time = time.time()

    # Using asyncio.run to run the asynchronous wait_n function
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
