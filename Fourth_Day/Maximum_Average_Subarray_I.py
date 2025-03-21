class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = 0
        for i in range(k):
            curr += nums[i]

        ans = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)

        return ans / k



if __name__ == '__main__':
    solution = Solution()
    nums = [1 , 12, -5, -6, 50, 3]
    k = 4

    result = solution.findMaxAverage(nums, k)
    print(result)