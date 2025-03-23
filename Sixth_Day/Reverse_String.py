class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1
        return s


if __name__ == '__main__':
    solution = Solution()
    s = ["h", "e", "l", "l", "o"]
    print(solution.reverseString(s))