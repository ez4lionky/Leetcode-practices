class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator, denominator = 0, 1
        i, n = 0, len(expression)
        while i < n:
            numerator1, sign = 0, 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                numerator1 = numerator1 * 10 + int(expression[i])
                i += 1
            numerator1 = sign * numerator1
            i += 1

            denominator1 = 0
            while i < n and expression[i].isdigit():
                denominator1 = denominator1 * 10 + int(expression[i])
                i += 1

            numerator = numerator * denominator1 + numerator1 * denominator
            denominator *= denominator1
        if numerator == 0:
            return "0/1"
        g = gcd(abs(numerator), denominator)
        return f"{numerator // g}/{denominator // g}"

