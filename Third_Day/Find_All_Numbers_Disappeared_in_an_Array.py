def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    present = set(nums)

    return [num for num in range(1, n + 1) if num not in present]

if __name__ == '__main__':
    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(arr))