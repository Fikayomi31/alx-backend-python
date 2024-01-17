#!/usr/bin/env python3
"""altering of some code into new function"""
import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:

    """return list of all the delays float values
    Args:
        n - an int range number
        max_delay - an int delay time passed
    """
    list_delay = [task_wait_random(max_delay) for _ in range(n)]
    # gather run the loop result concurrently
    return sorted(await asyncio.gather(*list_delay))
