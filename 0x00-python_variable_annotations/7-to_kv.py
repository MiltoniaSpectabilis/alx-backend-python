#!/usr/bin/env python3
"""
This module contains an annotated function that returns a tuple with
a squared second element.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the second element squared."""
    return (k, v ** 2)
