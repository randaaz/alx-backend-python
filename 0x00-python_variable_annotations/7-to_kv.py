#!/usr/bin/env python3
""" function to create a key-value tuple with the square of the value"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns: Tuple[str, float].
    """

    return (k, v**2)
