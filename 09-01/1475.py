class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        # for i in range(len(prices)):
        #     p = prices[i]
        #     while s and prices[s[-1]] > p:
        for i in range(len(prices)-1, -1, -1):
            p = prices[i]
            while s and s[-1] > p:
                s.pop()
            if s:
                prices[i] -= s[-1]
            s.append(p)
        return prices
        
