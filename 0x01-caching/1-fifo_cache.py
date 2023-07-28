#!/usr/bin/python3
"""
Acaching system that inherits from BaseCashing
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Is a caching system
    """

    def __init__(self):
        """init method
        """
        super().__init__()

    def put(self, key, item):
        """
        add data to cache and discard
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

            self.cache_data.update({key: item})

    def get(self, key):
        """
        Returns the value of cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
