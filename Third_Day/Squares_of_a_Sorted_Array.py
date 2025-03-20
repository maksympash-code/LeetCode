# def sortedSquares(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     n = len(nums)
#
#     for i in range(n):
#         nums[i] = nums[i] ** 2
#
#     return sorted(nums)

# def sortedSquares(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     n = len(nums)
#     m = len(nums) // 2
#
#     left, right = 0, n - 1
#
#     while left < right:
#         nums[left], nums[right] = nums[left] ** 2, nums[right] ** 2
#         left += 1
#         right -= 1
#
#     if len(nums) % 2 == 1:
#         nums[m] **= 2
#     return sorted(nums)


def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    ans = [0] * n

    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) >= abs(nums[right]):
            ans[i] = nums[left] * nums[left]
            left += 1
        else:
            ans[i] = nums[right] * nums[right]
            right -= 1

    return ans


if __name__ == '__main__':
    arr = [-7,-3,2,3,11]
    print(sortedSquares(arr))
