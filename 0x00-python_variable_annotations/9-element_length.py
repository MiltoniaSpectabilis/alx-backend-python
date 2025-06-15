#!/usr/bin/env python3
"""
This module contains an annotated function that returns
a list of tuples containing elements and their length
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list tuples each containing an element and its length."""
    return [(i, len(i)) for i in lst]
