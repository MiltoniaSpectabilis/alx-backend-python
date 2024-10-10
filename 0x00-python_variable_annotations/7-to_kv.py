#!/usr/bin/env python3

"""Defines a type-annotated function to_kv"""


def to_kv(k: str, v: str) -> list:
    """Returns a list of key-value pairs"""
    return [(k, int(v))]
