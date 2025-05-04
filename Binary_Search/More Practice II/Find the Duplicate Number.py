class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1
        r = len(nums)

        while l < r:
            mid = l + (r - l) // 2
            count = sum(x <= mid for x in nums)
            if count > mid:
                r = mid
            else:
                l = mid + 1
        return l

if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 4, 2, 2]
    print(s.findDuplicate(nums))