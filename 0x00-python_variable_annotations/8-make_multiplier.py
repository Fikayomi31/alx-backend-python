#!/usr/bin/env python3
"""Annotation function"""
from typing import Callable


def  make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""

    def muilt(m: float) -> float:
        """Return """
        return m * multiplier
    return muilt
    