#!/usr/bin/env python3
"""Annotation function"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return """
    return [(i, len(i)) for i in lst]
