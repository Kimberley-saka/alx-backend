#!/usr/bin/python3
"""
A caching system
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    delets least frequently used
    """
    def __init__(self):
        super().__init__()
        self.frequency = defaultdict(OrderedDict)
        self.min_frequency = 0

    def update_frequency(self, key):
        """
        updates frequency of use
        """
        frequency = len(self.frequency[key])
        del self.frequency[key][key]
        if not self.frequency[key] and frequency == self.min_frequency:
            self.min_frequency += 1
        self.frequency[key][key] = None

    def put(self, key, item):
        """
        remove data
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_key, _ = next(iter(self.frequency[self.cache_data.popitem(last=False)[0]]))
            print("DISCARD:", lfu_key)

        self.cache_data[key] = item
        self.frequency[key][key] = None
        self.min_frequency = 1

    def get(self, key):
        """
        get cache_data
        """
        if key is None or key not in self.cache_data:
            return None

        self.update_frequency(key)
        return self.cache_data[key]
