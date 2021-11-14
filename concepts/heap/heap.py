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
        while new_index < self.real_size and new_index <= (self.real_size // 2):
            left_child = (new_index * 2)
            right_child = (new_index * 2) + 1
            print(new_index, self.real_size, self.heap)
            if not self.heap[left_child] and not self.heap[right_child]:
                return key
            if self.heap[left_child] and self.heap[right_child]:
                print("Both present")
                if self.heap[new_index] > self.heap[left_child] and self.heap[left_child] < self.heap[right_child]:
                    print("Left replace ")
                    self.heap[new_index], self.heap[left_child] = self.heap[left_child], self.heap[new_index]
                    new_index = left_child
                elif self.heap[new_index] > self.heap[right_child] and self.heap[left_child] > self.heap[right_child]:
                    print("Right replace ")
                    self.heap[new_index], self.heap[right_child] = self.heap[right_child], self.heap[new_index]
                    new_index = right_child
                else:
                    break
            elif self.heap[left_child]:
                print("Only left present")
                print(self.heap[new_index], self.heap[left_child])
                print("printed left compariosn")
                if self.heap[new_index] > self.heap[left_child]:
                    self.heap[new_index], self.heap[left_child] = self.heap[left_child], self.heap[new_index]
                    new_index = left_child
                else:
                    return key
        return key

    def peek(self):
        if self.real_size > 0:
            return self.heap[1]
        print("No values to pop")
        return


def heapsort(ll):
    m = Heap(len(ll), "min")
    for item in ll:
        m.add(item)
    ans = []
    print(m.heap)
    for i in range(len(ll)):
        ans.append(m.pop())
        print(ans)
        print(m.heap)
        print(m.real_size)
    return ans


print(heapsort([5, 3, 6, 1, 9, 2, 7, 4, 10, 20, 12]))

