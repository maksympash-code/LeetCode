class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        new = ''
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        for i in range(len(strs)):
            if i < len(first) and first[i] == last[i]:
                new += first[i]
            else:
                break
        return new


if __name__ == '__main__':
    s = Solution()
    strs = ["flower","flow","flight"]

    print(s.longestCommonPrefix(strs))
