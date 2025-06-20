#!/usr/bin/env python3
"""
This module contains an annotated function that
safely returns the first element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence or None if it's empty."""
    if lst:
        return lst[0]
    else:
        return None
