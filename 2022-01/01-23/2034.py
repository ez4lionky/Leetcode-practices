# complicated version (if need to return both timestamp and price):
# two sorted linked list with Node ts: ; price: ;
# hash table with two types of Node 
# update: H[ts].A.price = V, H[ts].B.price = V
# if ts not in H, then insert timestamp and price into A and B
# if ts in H, then update and sort B
# here we only use dict and SortedList

from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
        self.items = {}  # key: timestamp, value: price
        self.max_ts = 0
        self.sorted_prices = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.items.keys():
            if timestamp > self.max_ts:
                self.max_ts = timestamp
            self.items[timestamp] = price
            self.sorted_prices.add(price)
            return
        self.sorted_prices.discard(self.items[timestamp])
        self.items[timestamp] = price
        self.sorted_prices.add(price)
        return


    def current(self) -> int:
        return self.items[self.max_ts]

    def maximum(self) -> int:
        return self.sorted_prices[-1]

    def minimum(self) -> int:
        return self.sorted_prices[0]


if __name__ == '__main__':
    obj = StockPrice()
    obj.update(1, 10)
    print('obj.items: ', obj.items, 'max_ts: ', obj.max_ts, 'sorted_prices: ', obj.sorted_prices)
    obj.update(2, 5)
    print('obj.items: ', obj.items, 'max_ts: ', obj.max_ts, 'sorted_prices: ', obj.sorted_prices)
    print(obj.current())
    print(obj.maximum())
    obj.update(1, 3)
    print('obj.items: ', obj.items, 'max_ts: ', obj.max_ts, 'sorted_prices: ', obj.sorted_prices)
    print(obj.maximum())
    obj.update(4, 2)
    print('obj.items: ', obj.items, 'max_ts: ', obj.max_ts, 'sorted_prices: ', obj.sorted_prices)
    print(obj.minimum())


