class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n

        left = 0
        curWindowSum = 0
        diametr = 2 * k + 1

        for right in range(n):
            curWindowSum += nums[right]

            if right - left + 1 >= diametr:
                res[left + k] = curWindowSum // diametr
                curWindowSum -= nums[left]
                left += 1

        return res



if __name__ == '__main__':
    s = Solution()
    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k = 3

    result = s.getAverages(nums, k)
    print(result)