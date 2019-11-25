class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(x, self.getMin())))

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]

    def getMin(self):
        if len(self.stack) == 0:
            return float('inf')
        return self.stack[-1][1]


# # Your MinStack object will be instantiated and called as such:
# x = 5
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()