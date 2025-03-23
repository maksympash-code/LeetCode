class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        k = 1

        for i in range(1, n):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    print(s.removeDuplicates(nums))