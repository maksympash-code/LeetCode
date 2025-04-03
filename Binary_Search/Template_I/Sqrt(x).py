class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x

        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                l = mid + 1
            else:
                r = mid - 1
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(8))