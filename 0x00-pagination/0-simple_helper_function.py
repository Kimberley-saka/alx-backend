#!/usr/bin/env python3
"""
pagination, dealing with indexes
"""


def index_range(page: int, page_size: int) -> tuple[int]:
    """
    retirn start index and end index as a tuple
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
