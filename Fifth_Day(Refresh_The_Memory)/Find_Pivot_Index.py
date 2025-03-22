class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):

            if left_sum == total_sum - left_sum - num:
                return i

            left_sum += num

        return -1

if __name__ == '__main__':
    s = Solution()
    nums = [2,1,-1]

    result = s.pivotIndex(nums)
    print(result)