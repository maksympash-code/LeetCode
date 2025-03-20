def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    k = 1

    for i in range(1, n):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k



if __name__ == '__main__':
    arr = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(arr))