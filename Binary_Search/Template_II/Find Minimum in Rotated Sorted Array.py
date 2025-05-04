class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid

        return nums[l]

if __name__ == '__main__':
    s = Solution()
    nums = [3,4,5,1,2]
    print(s.findMin(nums))