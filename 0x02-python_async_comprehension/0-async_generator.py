#!/usr/bin/env python3
"""async_generator that takes no argument"""

import asyncio
import random


async def async_generator():
    """doc
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
