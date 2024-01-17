#!/usr/bin/env python3
"""import wait_random and write an async routine called wait_n
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return list of all the delays float values
    Args:
        n - an int range number
        max_delay - an int delay time passed
    """
    list_delay = [asyncio.create_task(wait_random(max_delay))
                  for _ in range(n)]
    # gather run the loop result concurrently
    return sorted(await asyncio.gather(*list_delay))
