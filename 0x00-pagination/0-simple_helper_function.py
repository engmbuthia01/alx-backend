#!/usr/bin/env python3
def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start
    and end index for the given page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
