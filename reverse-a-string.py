def reverseStr(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    return "".join(s)
s=list(input())
print(reverseStr(s))