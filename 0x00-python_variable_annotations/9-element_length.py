#!/usr/bin/env python3
""" function to calculate the length of elements in an iterable of sequences"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Calculates the length of elements in an iterable of sequences. """
    return [(i, len(i)) for i in lst]
