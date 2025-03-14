class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in nums:
            i *= i
            arr.append(i)
        return sorted(arr)
