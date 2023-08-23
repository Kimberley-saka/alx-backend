#!/usr/bin/python3
"""
Least recently used cache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Laeast recently used cache
    """
    def __init__(self):
        """
        initialise
        """
        super().__init__()
        self.used_Keys = []

    def put(self, key, item):
        """
        add data to cache and/ delete it lru
        """
        if key is None or item is None:
            pass
        else:
            if key not in self.used_Keys:
                self.used_Keys.append(key)
            else:
                self.used_Keys.append(
                    self.used_Keys.pop(self.used_Keys.index(key)))
            size = len(self.cache_data)
            if size >= BaseCaching.MAX_ITEMS:
                discard_key = self.used_Keys.pop(0)
                self.cache_data.pop(discard_key)
                print('DISCARD: {}'.format(discard_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if key is not None and key in self.cache_data.keys():
            self.used_Keys.append(self.used_Keys.pop(self.used_Keys.index(key)))
            return self.cache_data.get(key)
        return None
