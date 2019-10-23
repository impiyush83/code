class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # inserting at start does this in O(1)
    def insert(self, value: int) -> None:
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def print(self) -> None:
        temp = self.head
        print("Linked List values are : ", end="  ")
        while temp is not None:
            print(temp.value, end='->')
            temp = temp.next
        print('NULL')

    # O(n)
    def delete(self, value: int) -> None:
        if self.search(value):
            temp = self.head
            if temp.value == value:
                self.head = self.head.next
            else:
                prev = None
                while temp is not None:
                    if temp.value == value:
                        prev.next = temp.next
                        temp.next = None
                        break
                    prev = temp
                    temp = temp.next

    # O(n)
    def search(self, key: int) -> bool:
        temp = self.head
        if temp is None:
            return None
        while temp is not None:
            if temp.value == key:
                return True
            temp = temp.next
        return False


s = SinglyLinkedList()
s.insert(5)
s.insert(4)
s.insert(3)
s.print()
print(s.search(4))
print(s.search(3))
s.delete(4)
s.print()
s.delete(5)
s.print()
s.delete(3)
s.print()

# tewsting git
