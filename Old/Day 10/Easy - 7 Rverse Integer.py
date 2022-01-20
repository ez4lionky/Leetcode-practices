def reverse(x: int) -> int:
    if x < -2**31 or x > 2**31 - 1:
        return 0
    s = str(x)
    if s[0] == '-':
        result = -int(s[1:][::-1])
    else:
        result = int(s[::-1])
    if result < -2**31 or result > (2**31 - 1):
        return 0
    return result


print(reverse(1534236469))
