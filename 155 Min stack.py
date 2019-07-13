# The key is the O(1) algorithm complexity, so we should get the minimum value at each time of push operation.
# But the pop operation will may change the minimum value.
# Therefore, we should store the minimum value sequence for every change.

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.size==0:
            self.min.append(x)
            self.size = self.size + 1
            return
        if x < self.min[self.size-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[self.size-1])
        self.size = self.size + 1

    def pop(self) -> int:
        if self.size==0:
            return None
        else:
            self.size = self.size - 1
            self.min.pop(-1)
            return self.stack.pop(-1)

    def top(self) -> int:
        if self.size==0:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min[self.size-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())

# Summary: Python can use tuple to store the current minimum value and data.
# Ref: Discussion in leetcode - https://leetcode.com/problems/min-stack/discuss/49022/My-Python-solution