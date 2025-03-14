class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        counter = 0

        for i in range(n):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
        return counter