#!/usr/bin/env python3
"""
Module with a function to create an asyncio.Task for wait_random.
"""

import asyncio
from typing import Callable

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function to create an asyncio.Task
    for wait_random with the specified max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
