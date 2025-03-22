class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        n, m = len(matrix), len(matrix[0])

        top, bottom = 0, n - 1
        left, right = 0, m - 1

        i = j = direction = 0

        for _ in range(n * m):
            res.append(matrix[i][j])

            if direction == 0:
                if j == right:
                    direction = 1
                    top += 1
                    i += 1
                else:
                    j += 1
            elif direction == 1:
                if i == bottom:
                    direction = 2
                    right -= 1
                    j -= 1
                else:
                    i += 1
            elif direction == 2:
                if j == left:
                    direction = 3
                    bottom -= 1
                    i -= 1
                else:
                    j -= 1
            else:
                if i == top:
                    direction = 0
                    left += 1
                    j += 1
                else:
                    i -= 1
        return res




if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    res = s.spiralOrder(matrix)
    print(res)