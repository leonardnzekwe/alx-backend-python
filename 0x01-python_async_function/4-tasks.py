#!/usr/bin/env python3
"""
Module with a function to create asyncio.Tasks for wait_random in parallel.
"""

from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create asyncio.Tasks for wait_random
    in parallel and return the list of delays.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    return delays
