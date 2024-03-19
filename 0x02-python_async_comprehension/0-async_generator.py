#!/usr/bin/env python3
"""
    Coroutine that loops 10 times and yields a random
    number between 0 and 10.
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Coroutine that loops 10 times and yields a random
        number between 0 and 10."""
    for _ in range(0,10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
