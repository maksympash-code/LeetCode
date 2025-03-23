class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        strs = sorted(strs)
        first, last = strs[0], strs[-1]

        for i in range(len(first)):
            if i < len(first) and first[i] == last[i]:
                res += first[i]
            else:
                break

        return res


if __name__ == '__main__':
    s = Solution()
    strs = ["flower","flow","flight"]
    print(s.longestCommonPrefix(strs))