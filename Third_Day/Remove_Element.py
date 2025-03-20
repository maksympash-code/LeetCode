def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    n = len(nums)
    k = 0

    for i in range(n):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


if __name__ == '__main__':
    arr = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(removeElement(arr, val))