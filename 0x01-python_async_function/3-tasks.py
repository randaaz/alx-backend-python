#!/usr/bin/env python3
""" Create an asyncio Task for a coroutine with a random delay. """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Create an asyncio Task for wait_random coroutine. """
    task = create_task(wait_random(max_delay))
    return task
