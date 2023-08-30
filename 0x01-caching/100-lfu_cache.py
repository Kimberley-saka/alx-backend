#!/usr/bin/python3
"""
Least frequently used cache
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching and is a caching system using LFU strategy
    """
    def __init__(self):
        """ Initialize the LFUCache
        """
        super().__init__()
        self.frequencies = []  # Store the frequencies in a list, each index corresponds to a key

    def put(self, key, item):
        """ Add an item in the cache using LFU strategy
        """
        if key is not None and item is not None:
            # Check if cache is full
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.frequencies)
                least_frequent_keys = [
                    k for k, v in enumerate(self.frequencies) if v == min_frequency
                ]
                least_recently_used_key = min(
                    least_frequent_keys,
                    key=lambda k: self.cache_data[k].get("last_used"),
                )
                del self.cache_data[least_recently_used_key]
                del self.frequencies[least_recently_used_key]
                print("DISCARD:", least_recently_used_key)

            # Add the new item to the cache
            self.cache_data[key] = {"value": item, "last_used": 0}
            self.frequencies.append(0)

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key in self.cache_data:
            idx = list(self.cache_data.keys()).index(key)
            self.frequencies[idx] += 1
            self.cache_data[key]["last_used"] += 1
            return self.cache_data[key]["value"]
        return None
