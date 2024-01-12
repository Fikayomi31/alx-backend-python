#!/usr/bin/env python3
"""Annotation function"""
from typing import List


def sum_mixed_list(mxd_list: List[int, float]) -> float:
    """Return a list of int and float as float"""
    return sum(mxd_list)
