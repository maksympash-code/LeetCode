def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    n = len(s)

    left = 0
    right = n - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    print(reverseString(s))