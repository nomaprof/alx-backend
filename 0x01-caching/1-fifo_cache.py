#!/usr/bin/env python3
"""
First in First Out FIFO Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    a class FIFOCache that inherits from BaseCaching for the purpose of FIFO
    """

    def __init__(self):
        """
        Init method for FIFO
        """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data for the purpose of caching
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        return the value in self.cache_data linked to key for caching
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
