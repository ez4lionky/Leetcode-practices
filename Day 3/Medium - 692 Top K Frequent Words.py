# The solution is similar to the 215, but here is to find top K.
# So we don't need to maintain a k-size heap, the two methods are the same time complexity.
import heapq


class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        freqs = {}
        for i in words:
            freqs[i] = words.count(i)

        MaxHeap = [(-freq, word) for word, freq in freqs.items()]   # python sorts the list of tuples by every field
        kfreq = [heapq.heappop(MaxHeap)[1] for _ in range(k)]
        return kfreq

sol = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(sol.topKFrequent(words, k))
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(sol.topKFrequent(words, k))

# Summary:
# we can use Collections.count to count the frequency of each word.
