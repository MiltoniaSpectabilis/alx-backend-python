#!/usr/bin/env python3
"""Module demonstrating function closures with type-annotation."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies its input by the given multiplier."""
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
