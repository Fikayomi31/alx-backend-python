#!/usr/bin/env python3
"""async_comprehension and parallel """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measuring the total run time of async_comprehension
    4x
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension()
                         )
    end = time.perf_counter() - start
    return end
