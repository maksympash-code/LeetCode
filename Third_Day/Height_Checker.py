def heightChecker(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    n = len(heights)
    counter = 0
    s_heights = sorted(heights)

    for i in range(n):
        if s_heights[i] != heights[i]:
            counter += 1

    return counter


if __name__ == '__main__':
    arr = [1,1,4,2,1,3]
    print(heightChecker(arr))