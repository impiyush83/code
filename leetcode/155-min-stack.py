class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ll = []

    def push(self, x: int) -> None:
        self.ll.append(x)

    def pop(self) -> None:
        self.ll.pop()

    def top(self) -> int:
        if self.ll:
            return self.ll[-1]

    def getMin(self) -> int:
        return min(self.ll)


# Your MinStack object will be instantiated and called as such:
x = 5
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()