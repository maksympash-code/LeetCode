class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = 0
        startValue = 1

        for num in nums:
            prefix_sum += num
            startValue = max(startValue, 1 - prefix_sum)

        return startValue



if __name__ == '__main__':
    s = Solution()
    nums = [-3,2,-3,4,2]

    result = s.minStartValue(nums)
    print(result)