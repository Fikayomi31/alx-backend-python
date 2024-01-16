#!/usr/bin/env python3
"""function that takes no arguments"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    return [value async for value in async_generator()]
