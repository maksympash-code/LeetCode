class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        k = 0

        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(s.removeElement(nums, val))