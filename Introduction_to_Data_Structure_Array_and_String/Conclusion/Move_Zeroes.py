class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = 0

        for i in range(n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        for i in range(k, n):
            nums[i] = 0

        return nums

if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,0,3,12]
    print(solution.moveZeroes(nums))