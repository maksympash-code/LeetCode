def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    distinct = set(nums)

    if len(distinct) < 3:
        return max(distinct)

    distinct.remove(max(distinct))
    distinct.remove(max(distinct))

    return max(distinct)


if __name__ == '__main__':
    arr = [2,2,3,1]
    print(thirdMax(arr))