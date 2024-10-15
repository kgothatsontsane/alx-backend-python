#!/usr/bin/env python3
"""Module to create asyncio tasks"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task for wait_random with the specified
    max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A task that will run wait_random with the
        given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
