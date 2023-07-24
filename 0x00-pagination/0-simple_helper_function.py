#!/usr/bin/env python3
"""
Function index_range that takes in twe integer arguments page
and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of integers
    """
    return ((page-1) * page_size, page_size * page)
