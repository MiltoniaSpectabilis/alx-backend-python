#!/usr/bin/env python3

"""Defines a type-annotated function safely_get_value."""

from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely gets the value from a dictionary for a given key,
    or returns a default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default