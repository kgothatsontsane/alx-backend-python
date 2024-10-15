#!/usr/bin/env python3
"""
This module contains asynchronous functions to wait
for random delays.
"""

import asyncio
from typing import List
from random import uniform


async def task_wait_random(max_delay: int) -> float:
    """
    Asynchronously wait for a random delay between 0
    and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The actual delay.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously wait for n random delays and return them sorted.

    Args:
        n (int): The number of delays.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    sorted_delays = sorted(delays)
    return sorted_delays
