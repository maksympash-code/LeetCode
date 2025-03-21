class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        prefix_sum = [0] * n

        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        return prefix_sum



if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]

    result = s.runningSum(nums)
    print(result)
