#!/usr/bin/env python3
"""function to return the class"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int):
    """Return asyncio.task"""
    return asyncio.create_task(wait_random(max_delay))
