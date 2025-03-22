class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = -1
        second_largest = -1
        index = -1

        for i, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                index = i
            elif num > second_largest:
                second_largest = num

        if largest >= 2 * second_largest:
            return index
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4]

    result = s.dominantIndex(nums)
    print(result)