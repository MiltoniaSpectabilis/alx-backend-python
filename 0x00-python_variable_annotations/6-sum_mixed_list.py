#!/usr/bin/env python3
"""
This module contains a function that returns
the sum of a list of mixed types with annotations.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of mixed types"""
    return sum(mxd_lst)
