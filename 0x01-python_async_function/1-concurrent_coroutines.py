#!/usr/bin/env python3

"""Executes multiple coroutines"""

from typing import List
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay"""
    futures = [wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
