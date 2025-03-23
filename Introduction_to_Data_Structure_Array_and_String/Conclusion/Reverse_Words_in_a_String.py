class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = s.split()[::-1]
        res = []

        for i in tmp:
            res.append(i)

        return ' '.join(res)



# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
        # res = []
        # for i in s.split():
        #     res.append(i)
        #
        # left = 0
        # right = len(res) - 1
        #
        # while left < right:
        #     res[left], res[right] = res[right], res[left]
        #     left += 1
        #     right -= 1
        #
        #
        # return ' '.join(res)


if __name__ == '__main__':
    solve = Solution()
    s = "the sky is blue"
    print(solve.reverseWords(s))