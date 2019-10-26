class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 3 pointer method - iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current is not None:
            next_element = current.next
            current.next = prev
            prev = current
            current = next_element
        head = prev
        return head



# recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current is not None:
            next_element = current.next
            current.next = prev
            prev = current
            current = next_element
        head = prev
        return head