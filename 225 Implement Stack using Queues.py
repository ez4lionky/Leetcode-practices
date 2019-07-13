# The question means the storage of data is using the queue.
# There are three methods in total.
# The first two methods implement the stack by using two queues.
# 1. Push O(n), Pop O(1)
# Each time before push the element, we remove all elements of current queue into a new queue,
# then push the element and temporary queue's elements.
# 2. Push O(1), Pop O(n)
# Each time pop the element, using a new queue to store the element without the final one.

# 3. The third methods only use one queue, when every time push the element into queue(stack)
# remove top element from front to rear recursively
# here is the implementation of third method (Push O(n), can also use Pop O(n)).

class MyQueue:
    def __init__(self):
        self.size = 0
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size = self.size + 1

    def pop(self) -> int:
        if self.queue:
            self.size = self.size - 1
            return self.queue.pop(0)
        else:
            return None

    def empty(self) -> bool:
        if self.size==0:
            return True
        else:
            return False

    def peek(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return None


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = MyQueue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.push(x)
        size = self.stack.size
        while size > 1:
            t = self.stack.pop()
            self.stack.push(t)
            size = size - 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.stack.size != 0:
            return self.stack.peek()
        else:
            return None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stack.empty()

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push([1])
obj.push([2])
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2, param_3, param_4)