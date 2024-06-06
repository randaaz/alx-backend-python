#!/usr/bin/env python3

""" calculate the sum of a list of mixed integers and floats """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  Calculates the sum of a list of mixed integers and floats. """
    return float(sum(mxd_lst))
