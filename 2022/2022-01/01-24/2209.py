# vanilla queue version
# class CQueue:
#
#     def __init__(self):
#         self.queue = []
#         self.start = 0
#
#     def appendTail(self, value: int) -> None:
#         self.queue.append(value)
#
#
#     def deleteHead(self) -> int:
#         if self.start == len(self.queue):
#             return -1
#         v = self.queue[self.start]
#         self.start += 1
#         return v


# double stacks implement queue
class CQueue:
    def __init__(self):
        self.stack0 = []
        self.stack1 = []

    def appendTail(self, value: int) -> None:
        self.stack0.append(value)

    def deleteHead(self) -> int:
        if len(self.stack0) + len(self.stack1) == 0:
            return -1
        if len(self.stack1) != 0:
            v = self.stack1.pop(-1)
            return v
        for _ in range(len(self.stack0)):
            t = self.stack0.pop(-1)
            self.stack1.append(t)
        v = self.stack1.pop(-1)
        return v


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
