from sortedcontainers import SortedDict


class MyCalendar:

    def __init__(self):
        self.cal = SortedDict()

    def book(self, start: int, end: int) -> bool:
        i = self.cal.bisect_left(end)
        if i == 0 or self.cal.items()[i-1][1]<=start:
            self.cal[start] = end
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
