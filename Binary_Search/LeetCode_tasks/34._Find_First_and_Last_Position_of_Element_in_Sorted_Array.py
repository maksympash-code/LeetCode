class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        res = [-1, -1]

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res[0] = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res[1] = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [5, 7, 7, 8, 8, 10]
    target = 8
    print(s.searchRange(arr, target))