# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1

        l = 1
        r = n

        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            elif not isBadVersion(mid):
                l = mid + 1

        if isBadVersion(l):
            return l