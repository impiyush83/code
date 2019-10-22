# LRU with Queue and Dictionary
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapper = dict()
        self.queuer = []

    def get(self, key: int) -> int:
        if not self.mapper.get(key):
            return -1
        self.queuer.remove(key)
        self.queuer.insert(0, key)
        return self.mapper.get(key)

    def put(self, key: int, value: int) -> None:
        if self.mapper.get(key):
            self.mapper[key] = value
            self.queuer.remove(key)
            self.queuer.insert(0, key)
        else:
            if self.capacity == len(self.mapper):
                self.mapper.pop(self.queuer[-1])
                self.queuer.remove(self.queuer[-1])
            self.queuer.insert(0, key)
            self.mapper[key] = value


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
