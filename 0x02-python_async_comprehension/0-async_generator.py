#!/usr/bin/env python3

""" An asynchronous generator that yields 10 random float numbers """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Asynchronous generator that yields random numbers. """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
