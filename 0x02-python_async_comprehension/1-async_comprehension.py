#!/usr/bin/env python3

""" Asynchronous comprehension to collect random float
numbers from an async generator. """

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collects 10 random float numbers from the async
    generator using an async comprehension. """
    a = [i async for i in async_generator()]
    return a
