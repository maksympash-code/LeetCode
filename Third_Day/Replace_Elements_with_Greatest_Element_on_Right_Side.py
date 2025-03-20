def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    n = len(arr)
    max_right = -1

    for i in range(n - 1, -1, -1):
        new_value = max_right
        max_right = max(max_right, arr[i])
        arr[i] = new_value

    return arr



if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    print(replaceElements(arr))

