#!/usr/bin/env python3
"""
Measuring the total runtime of executing
async_comprehension four times in parallel.
"""

from time import perf_counter
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension
    four times in parallel using asyncio.gather,
    and measures the total runtime.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    total_runtime = perf_counter() - start_time

    return total_runtime
