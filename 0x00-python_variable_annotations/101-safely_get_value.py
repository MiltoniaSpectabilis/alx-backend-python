#!/usr/bin/env python3
"""Module with a function to safely get a value from a mapping.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Returns value if found otherwise default."""
    if key in dct:
        return dct[key]
    else:
        return default
