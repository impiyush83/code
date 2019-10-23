class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def print(self):
        temp = self.head
        print("Linked List values are : ", end="  ")
        while temp is not None:
            print(temp.value, end='->')
            temp = temp.next
        print('NULL')

    def delete(self, value):
        temp = self.head
        if temp.value == value:
            self.head = self.head.next
        else:
            pass

    def search(self, key):
        temp = self.head
        if temp is None:
            return None
        while temp is not None:
            if temp.value == key:
                return 1
            temp = temp.next
        return 0


s = SinglyLinkedList()
s.insert(5)
s.insert(4)
s.print()
print(s.search(4))
print(s.search(3))
