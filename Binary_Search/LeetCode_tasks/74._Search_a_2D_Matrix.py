class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        n, m = len(matrix), len(matrix[0])

        top, botom = 0, n

        while top < botom:
            mid = top + (botom - top) // 2
            if matrix[mid][0] <= target:
                top = mid + 1
            else:
                botom = mid

        row = top - 1
        if row < 0:
            return False

        l, r = 0, m - 1
        while l < r:
            mid = l + (r - l) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid
        return l < m and matrix[row][l] == target