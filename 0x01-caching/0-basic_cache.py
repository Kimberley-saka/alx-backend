#!/usr/bin/python3
"""
Add items to cache and get item linked to key
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system
    """
    def __init__(self):
        """
        initialise
        """
        super().__init__()

    def put(self, key, item):
        """
        add data to cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
