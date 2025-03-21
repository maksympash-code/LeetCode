class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            total_sum -= num

            if left_sum == total_sum:
                return i

            left_sum += num

        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 7, 3, 6, 5, 6]

    result = s.pivotIndex(nums)
    print(result)