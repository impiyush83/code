

class OrderedStream:

    def __init__(self, n: int):
        self.store = [None] * (n + 1)
        self.current = 1

    def insert(self, idKey: int, value: str):
        self.store[idKey] = value
        res = []
        while self.current < len(self.store) and self.store[self.current]:
            res.append(self.store[self.current])
            self.current += 1
        return res


obj = OrderedStream(5)
print(obj.insert(3, 'ccccc'))
print(obj.insert(1, 'aaaaa'))
print(obj.insert(2, 'bbbbb'))
print(obj.insert(5, 'eeeee'))
print(obj.insert(4, 'ddddd'))