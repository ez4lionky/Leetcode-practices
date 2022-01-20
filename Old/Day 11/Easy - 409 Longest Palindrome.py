def longest_palindrome(s: str) -> int:
    return len(s) - max(sum(v & 1 for v in collections.Counter(s).values()) - 1, 0)


print(longest_palindrome('abccccdd'))
print(longest_palindrome('a'))
print(longest_palindrome('bb'))
print(longest_palindrome('bananas'))
