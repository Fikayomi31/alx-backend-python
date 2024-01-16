#!/usr/bin/env python3
"""function that takes no arguments"""

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    result = [value async for value in async_generator()]
    return result
