#!/usr/bin/env python3
"""Annotation function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple"""
    return k, v ** 2
