# My solution is obtained by observing the constraints of popped operation.
# The key idea of this problem is to judge the sequence by popped sequence.
# Specifically, the next popped element should be within a certain range of pushed sequence.
# The range is according to the index of current popped element in pushed sequence.
# i: pushed index of current popped element, range: pushed[i-1, :]

# The advantage of this method is tiny memory usage, but costs much more time.

class Solution:
    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
        index = 0
        while len(pushed)>1:
            pushed_index = pushed.index(popped[index])
            pushed.pop(pushed_index)
            if pushed_index==0:
                temp = pushed[0:]
            else:
                temp = pushed[pushed_index-1:]
            if popped[index+1] not in temp:
                return False
            index = index + 1
        return True

sol = Solution()
# pushed = [1, 2, 3, 4, 5]
# popped = [4, 5, 3, 2, 1]
# pushed = [1, 2, 3, 4, 5]
# popped = [4, 3, 5, 1, 2]
pushed = [2, 1, 0]
popped = [2, 1, 0]
print(sol.validateStackSequences(pushed, popped))

# Example 1:
# Input: pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# Example 2:
# Input: pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
# Output: false
# Explanation: 1 cannot be popped before 2.


# Summary:
# The common and less time complexity solution is using a stack to simulate the process of popped and pushed operation.
# This method is similar to infix expression stack. Push the every element of pushed sequence one by one,
# when the front of popped sequence matches the top of simulation stack, the simulation stack popes the top element,
# until the simulation stack is empty (that means the two sequences are matched).