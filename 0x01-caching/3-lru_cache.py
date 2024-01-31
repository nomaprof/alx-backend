#!/usr/bin/env python3
"""
Last rarely used LRU Caching
"""


from lib2to3.pgen2.token import BACKQUOTE
from typing import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching for the purpose of Caching
    """

    def __init__(self):
        """
        Init method for the purpose of caching
        """
        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data for caching
        """
        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.lru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.lru_order) > BaseCaching.MAX_ITEMS:
            self.lru_order.popitem(last=False)

    def get(self, key):
        """
        Must return the value in self.cache_data linked for caching
        """
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
