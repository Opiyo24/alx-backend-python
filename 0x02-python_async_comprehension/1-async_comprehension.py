#!/usr/bin/env python3

"""
    Coroutine that loops 10 times and yields a random number
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
        Coroutine that collects 10 random numbers
    """
    return [_ async for _ in async_generator()]