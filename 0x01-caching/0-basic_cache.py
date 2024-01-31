#!/usr/bin/env python3
"""
Basic dictionary for caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Base Cache class that inherits from BaseCaching for caching task
    """

    def put(self, key, item):
        """
        Must assign to the dictionary for caching
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key for caching
        """
        return self.cache_data.get(key, None)
