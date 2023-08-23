#!/usr/bin/python3
"""
Last in first out cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Last in first out cache
    """
    def __init__(self):
        """
        initialise
        """
        super().__init__()

    def put(self, key, item):
        """
        add data to cache and/ delete it
        """
        if key is None or item is None:
            pass
        else:
            size = len(self.cache_data)
            if size >= BaseCaching.MAX_ITEMS:
                last_item = self.cache_data.popitem()
                print('DISCARD: {}'.format(last_item[0]))

            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
