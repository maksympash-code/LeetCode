# def sortArrayByParity(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     left, right = 0, len(nums) - 1
#
#     while left < right:
#         if nums[left] % 2 == 0:
#             left += 1
#         elif nums[right] % 2 == 1:
#             right -= 1
#         else:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1
#
#     return nums


def sortArrayByParity(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    evens = [num for num in nums if num % 2 == 0]
    odds = [num for num in nums if num % 2 == 1]
    return evens + odds

if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    print(sortArrayByParity(arr))