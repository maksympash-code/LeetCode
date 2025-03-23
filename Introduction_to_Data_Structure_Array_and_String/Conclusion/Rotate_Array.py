class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # return nums[-k:] + nums[:-k]
        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = rotated[i]
        return nums



if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(s.rotate(nums, k))