class Heap:
    def __init__(self, heap_size, heap_type="max"):
        self.heap_size = heap_size
        self.heap = [0] * (heap_size + 1)
        self.real_size = 0
        if heap_type in ["max", "min"]:
            self.type = heap_type
        else:
            raise Exception("Invalid heap type")

    def add(self, key):
        if self.real_size > self.heap_size:
            print("Too many values added")
            return

        self.real_size += 1
        self.heap[self.real_size] = key
        new_item_index = self.real_size
        parent = new_item_index // 2
        if self.type == "max":
            while self.heap[new_item_index] > self.heap[parent] and \
                    new_item_index > 1:
                self.heap[new_item_index], self.heap[parent] \
                    = self.heap[parent], self.heap[new_item_index]
                new_item_index = parent
                parent = new_item_index // 2
        else:
            while self.heap[new_item_index] < self.heap[parent] and \
                    new_item_index > 1:
                self.heap[new_item_index], self.heap[parent] \
                    = self.heap[parent], self.heap[new_item_index]
                new_item_index = parent
                parent = new_item_index // 2

    def pop(self):
        if self.real_size < 1:
            print("No values to pop")
            return
        key = self.heap[1]
        self.heap[1] = self.heap[self.real_size]
        self.heap[self.real_size] = 0
        self.real_size -= 1
        new_index = 1
        print(self.heap)
        while new_index < self.real_size and new_index <= self.real_size // 2:
            left_child = (new_index * 2)
            right_child = (new_index * 2) + 1
            if self.type == "max":
                if self.heap[new_index] < self.heap[left_child] or self.heap[new_index] < self.heap[right_child]:
                    if self.heap[left_child] < self.heap[right_child]:
                        self.heap[new_index], self.heap[right_child] \
                            = self.heap[right_child], self.heap[new_index]
                        new_index = right_child
                    else:
                        self.heap[new_index], self.heap[left_child] \
                            = self.heap[left_child], self.heap[new_index]
                        new_index = left_child
                else:
                    break
            else:
                if self.heap[new_index] > self.heap[left_child] or self.heap[new_index] > self.heap[right_child]:
                    if self.heap[left_child] < self.heap[right_child]:
                        self.heap[new_index], self.heap[left_child] \
                            = self.heap[left_child], self.heap[new_index]
                        new_index = left_child
                    else:
                        self.heap[new_index], self.heap[right_child] \
                            = self.heap[right_child], self.heap[new_index]
                        new_index = right_child
                else:
                    break
        return key

    def peek(self):
        if self.real_size > 0:
            return self.heap[1]
        print("No values to pop")
        return


m = Heap(6, "min")
m.add(1)
m.add(5)
m.add(2)
m.add(3)
m.add(4)
m.pop()
print(m.heap)