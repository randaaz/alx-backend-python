#!/usr/bin/env python3
""" function to calculate the sum of a list of floats """
from typing import Callable, Iterator, Union, Optional, List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of the numbers in the input list.
    """

    return sum(input_list)
