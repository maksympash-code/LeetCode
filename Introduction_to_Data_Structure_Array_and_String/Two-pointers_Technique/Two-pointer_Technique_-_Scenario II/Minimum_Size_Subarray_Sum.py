class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        curr = 0
        res = float('inf')

        for right in range(0, len(nums)):
            curr += nums[right]

            while curr >= target:
                res = min(res, right - left + 1)
                curr -= nums[left]
                left += 1
        return res if res != float('inf') else 0


if __name__ == '__main__':
    s = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(s.minSubArrayLen(target, nums))