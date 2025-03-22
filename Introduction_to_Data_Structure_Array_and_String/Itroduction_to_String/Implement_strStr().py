class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i: i + m] == needle:
                return i

        return -1




if __name__ == '__main__':
    s = Solution()
    haystack = "sadbutsad"
    needle = "sad"

    print(s.strStr(haystack, needle))