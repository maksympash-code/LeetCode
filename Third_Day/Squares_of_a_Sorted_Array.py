def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)

    for i in range(n):
        nums[i] = nums[i] ** 2

    return sorted(nums)

if __name__ == '__main__':
    arr = [-4, -1, 0, 3, 10]
    print(sortedSquares(arr))
