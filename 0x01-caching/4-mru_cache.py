#!/usr/bin/python3
"""
Acaching system that inherits from BaseCashing
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    remove most recently used item in cache
    """

    def __init__(self):
        """
        init
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        remove least reacently used
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        get cache_data
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
