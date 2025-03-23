class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = []
        k = 0

        for i in range(n):
            if nums[i] == 1:
                k += 1
            elif nums[i] == 0:
                k = 0
            res.append(k)

        return max(res)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 0, 1, 1, 1]
    print(s.findMaxConsecutiveOnes(nums))