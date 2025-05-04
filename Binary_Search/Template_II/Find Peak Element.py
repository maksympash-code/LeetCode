class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
        return l


if __name__ == '__main__':
    s = Solution()
    arr = [1,2,1,3,5,6,4]
    print(s.findPeakElement(arr))