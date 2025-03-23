class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        res = []


        for word in words:
            res.append(word[::-1])
            # lst = list(word)
            # left = 0
            # right = len(word) - 1
            # while left < right:
            #     lst[left], lst[right] = lst[right], lst[left]
            #     left += 1
            #     right -= 1
            # res.append(''.join(lst))


        return ' '.join(res)


if __name__ == '__main__':
    solve = Solution()
    s = "Let's take LeetCode contest"
    print(solve.reverseWords(s))