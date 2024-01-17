#!/usr/bin/env python3
"""asynchronous coroutine that takes intefer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asyncio function that take an integer argument
    Args:
        max_delay - default value of 10
    Return: float
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
