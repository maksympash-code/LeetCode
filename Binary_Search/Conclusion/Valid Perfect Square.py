class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 1
        r = num

        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                l = mid + 1
            else:
                r = mid - 1
        return False