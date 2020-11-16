def keep_alphanumeric(s: str):
    r = ''
    for i in s:
        if i.isalnum():
            r += i
    return str(r)


def is_palindrome(s: str):
    if s is '':
        return True
    s = keep_alphanumeric(s)
    s = s.lower()
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def opt_is_palindrome(s: str):
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


print(opt_is_palindrome('race a car'))
print(opt_is_palindrome('A man, a plan, a canal: Panama'))
print(opt_is_palindrome(''))
print(opt_is_palindrome('tenet'))
