#!/usr/bin/env python3
"""Annotation function"""
from typing import Sequence, Tuple, List


def element_length(lst: Sequence[int]) -> List[Tuple[Sequence, int]]:
    """return """
    return [(i, len(i)) for i in lst]
