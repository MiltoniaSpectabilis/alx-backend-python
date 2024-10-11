#!/usr/bin/env python3

"""Defines a type-annotated function zoom_array."""


from typing import Tuple, List, TypeVar, Union

T = TypeVar('T')


def zoom_array(lst: Tuple[T, ...], factor: int = 2) -> List[T]:
    """
    Repeats each element in the tuple a specified number of times.
    """
    zoomed_in: List[T] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))
zoom_3x = zoom_array(tuple(array), 3)

print(zoom_2x)
print(zoom_3x)
