#!/usr/bin/env python3
"""function that takes no arguments"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension()i -> float:
    result = [value async for value in async_generator()]
    return result
