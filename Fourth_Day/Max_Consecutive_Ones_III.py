class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1




if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2

    result = s.longestOnes(nums, k)
    print(result)