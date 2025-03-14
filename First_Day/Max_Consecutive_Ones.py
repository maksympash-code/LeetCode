class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        arr = []
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            elif nums[i] == 0:
                counter = 0
            arr.append(counter)
        return max(arr)
