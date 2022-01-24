# from sortedcontainers import SortedList

# vanilla version, use extra SortedList to find min value
# and time complexity O(logn)
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
#         self.sl = SortedList()
#
#     def push(self, x: int) -> None:
#         self.data.append(x)
#         self.sl.add(x)
#
#     def pop(self) -> None:
#         v = self.data.pop(-1)
#         self.sl.remove(v)
#         return v
#
#     def top(self) -> int:
#         return self.data[-1]
#
#
#     def min(self) -> int:
#         return self.sl[0]


# create additional stack to store min value, faster (push, pop, top, min O(1))
# but space complexity can be optimized
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
#         self.mins = []
#
#     def push(self, x: int) -> None:
#         self.data.append(x)
#         if len(self.mins) == 0:
#             self.mins.append(x)
#         elif x <= self.mins[-1]:
#             self.mins.append(x)
#
#     def pop(self) -> None:
#         v = self.data.pop(-1)
#         if v == self.mins[-1]:
#             self.mins.pop(-1)
#         return v
#
#     def top(self) -> int:
#         return self.data[-1]
#
#     def min(self) -> int:
#         return self.mins[-1]

# Third version: 
# use additional stack save indices instead of value (so that we can avoid redundant values)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_ids = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.min_ids) == 0:
            self.min_ids.append(0)
        elif x < self.data[self.min_ids[-1]]:
            self.min_ids.append(len(self.data) - 1)

    def pop(self) -> None:
        cur_id = len(self.data) - 1
        v = self.data.pop(-1)
        if cur_id == self.min_ids[-1]:
            self.min_ids.pop(-1)
        return v

    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return self.data[self.min_ids[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-1)
    print(min_stack.min())
    print(min_stack.top())
    print(min_stack.pop())
    print(min_stack.min())

