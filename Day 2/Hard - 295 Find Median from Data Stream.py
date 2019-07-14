import heapq

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.MinHeap = []
        self.MaxHeap = []

    def addNum(self, num: int) -> None:
        lmin = len(self.MinHeap)
        lmax = len(self.MaxHeap)

        if lmin + lmax == 0:
            heapq.heappush(self.MaxHeap, -num)
        elif lmin == lmax:
            if num > -self.MaxHeap[0]:
                heapq.heappush(self.MinHeap, num)
            else:
                heapq.heappush(self.MaxHeap, -num)
        elif lmin < lmax:
            if num > -self.MaxHeap[0]:
                heapq.heappush(self.MinHeap, num)
            else:
                t = -heapq.heappop(self.MaxHeap)
                heapq.heappush(self.MinHeap, t)
                heapq.heappush(self.MaxHeap, -num)
        elif lmin>lmax:
            if num>self.MinHeap[0]:
                t = heapq.heappop(self.MinHeap)
                heapq.heappush(self.MaxHeap, -t)
                heapq.heappush(self.MinHeap, num)
            else:
                heapq.heappush(self.MaxHeap, -num)

    def findMedian(self) -> float:
        lmin = len(self.MinHeap)
        lmax = len(self.MaxHeap)

        if lmin == lmax:
            return (self.MinHeap[0] - self.MaxHeap[0]) / 2.0
        if lmin > lmax:
            return float(self.MinHeap[0])
        else:
            return float(-self.MaxHeap[0])


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())