#!/usr/bin/env python3
"""Annotation function"""
from typing import Mapping, Any, Union, T


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """return """
    if key in dct:
        return dct[key]
    else:
        return default
