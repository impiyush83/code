from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.lru = OrderedDict()

    def get(self, key):
        if not self.lru.get(key):
            return -1
        self.lru.move_to_end(key, True)
        return self.lru.get(key)

    def put(self, key, value):
        if self.lru.get(key):
            self.lru.move_to_end(key, True)
        self.lru[key] = value
        if len(self.lru) > self.capacity:
            self.lru.popitem(last=False)  # Pop first item


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
