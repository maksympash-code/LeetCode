class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        left = 0
        ans = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1

            ans += right - left + 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [10, 5, 2, 6]
    k = 100

    result = solution.numSubarrayProductLessThanK(nums, k)
    print(result)