class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r - l) // 2
            guess = nums[mid]
            if guess < target:
                l = mid + 1
            else:
                r = mid
        return l

if __name__ == '__main__':
    s = Solution()
    arr = [1, 3, 5, 6]
    print(s.searchInsert(arr, 7))
