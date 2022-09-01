# class OrderedStream:
#
#     def __init__(self, n: int):
#         self.n = n
#         self.data = {}
#         self.ptr = 1
#
#
#     def insert(self, idKey: int, value: str) -> List[str]:
#         res = []
#         self.data[idKey] = value
#         if idKey == self.ptr:
#             while idKey <= self.n:
#                 if idKey in self.data:
#                     res.append(self.data[idKey])
#                 else:
#                     break
#                 idKey += 1
#             self.ptr = idKey
#         return res


class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        stream_ = self.stream

        stream_[idKey] = value
        res = list()
        while self.ptr < len(stream_) and stream_[self.ptr]:
            res.append(stream_[self.ptr])
            self.ptr += 1
        
        return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
