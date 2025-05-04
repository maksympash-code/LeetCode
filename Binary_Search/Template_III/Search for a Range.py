class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        # знаходимо ліву межу
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        # перевіряємо, чи є target
        if l == n or nums[l] != target:
            return [-1, -1]
        left = l

        # знаходимо праву межу
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        right = r - 1

        return [left, right]

if __name__ == '__main__':
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    print(s.searchRange(nums, 8))
