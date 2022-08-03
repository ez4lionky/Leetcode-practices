class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.data = [None] * k
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
            self.data[self.front] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.data[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # value = self.data[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.front == -1:
            return -1
        return self.data[self.front]

    def Rear(self) -> int:
        if self.rear == -1:
            return -1
        return self.data[self.rear]

    def isEmpty(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def isFull(self) -> bool:
        if self.front == (self.rear + 1) % self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
