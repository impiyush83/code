class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        while True:
            if slow.next is None:
                return False

            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next

            if fast.next is None:
                return False

            fast = fast.next
            if fast == slow:
                return True
