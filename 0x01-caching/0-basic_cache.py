#!/usr/bin/python3
"""
Acaching system that inherits from BaseCashing
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Is a caching system
    """

    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """
        add data to cache
        """
        if key is not None or item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Returns the value of cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
