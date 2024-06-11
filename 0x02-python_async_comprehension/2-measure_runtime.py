#!/usr/bin/env python3

""" Measure the total runtime of running
four async comprehensions concurrently. """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """  Measure the runtime of executing four async
    comprehensions concurrently. """
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
