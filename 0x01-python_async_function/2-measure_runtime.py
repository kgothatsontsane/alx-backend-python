#!/usr/bin/env python3
"""Module to measure the runtime of wait_n"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return the average time per call.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each call to
        wait_n.

    Returns:
        float: The average execution time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
