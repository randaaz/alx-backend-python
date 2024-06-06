#!/usr/bin/env python3
""" This script defines a function to create a multiplier function"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns A function that multiplies its argument by the provided multiplier.
    """
    def f(n: float) -> float:
        """ Returns the result of multiplying """
        return float(n * multiplier)

    return f
