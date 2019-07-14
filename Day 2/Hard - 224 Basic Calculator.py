# The key idea is

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) ==0

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def push(self, a):
        self.items.append(a)

    def pop(self):
        return self.items.pop()

class Solution:
    def compute(self, n_s: Stack, o_s: Stack):
        if len(n_s.items)<2:
            return n_s, o_s

        num1 = n_s.pop()
        num2 = n_s.pop()

        if o_s.peek()=='+':
            n_s.push(num1 + num2)
        elif o_s.peek()=='-':
            n_s.push(num2 - num1)

        if o_s:
            o_s.pop()
        return n_s, o_s

    def calculate(self, s: str) -> int:
        number_stack = Stack()
        operator_stack = Stack()
        state = 0  # 0 presents the start state, 1 presents the number state, 2 presents the operator state
        compute_flag = False  # if compute according to the number and operator stack
        number = 0

        i = 0
        while i<len(s):
            if s[i] == ' ':
                i += 1
                continue

            # Start state
            if state==0:
                if '0'< s[i] < '9':
                    state = 1
                else:
                    state = 2
                i -= 1

            # Number state
            elif state==1:
                if '0'<= s[i] <= '9':
                    number = number * 10 + ord(s[i]) - ord('0')
                else:
                    number_stack.push(number)
                    if compute_flag:
                        number_stack, operator_stack = self.compute(number_stack, operator_stack)
                    state = 2
                    number = 0
                    i -= 1

            # Operator state
            else:
                if s[i]=='+' or s[i]=='-':
                    operator_stack.push(s[i])
                    compute_flag = True
                elif s[i]=='(':
                    compute_flag = False
                    state = 1
                elif '0'<= s[i] <= '9':
                    state = 1
                    i -= 1
                elif s[i]==')':
                    number_stack, operator_stack = self.compute(number_stack, operator_stack)

            i += 1

        # '123 + 456'
        if number!=0:
            number_stack.push(number)
            number_stack, operator_stack = self.compute(number_stack, operator_stack)

        # the situation of '0', and '123 + 0' will peek the number stack
        if number==0 and number_stack.isEmpty():
            return 0
        return number_stack.peek()

sol = Solution()

# s = "1 + 1"
# print(sol.calculate(s))
#
# s = " 2-1 + 2 "
# print(sol.calculate(s))
#
# s = " 123 + 0 "
# print(sol.calculate(s))
#
# s = "(1+(4+5+2)-3)+(6+8)"
# print(sol.calculate(s))
# Summary:
#