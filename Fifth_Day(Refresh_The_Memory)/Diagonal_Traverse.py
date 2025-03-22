class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n, m = len(mat), len(mat[0])
        res = []
        i = j = direction = 0

        for _ in range(n * m):
            res.append(mat[i][j])

            if direction == 0:
                if j == m - 1:
                    direction = 1
                    i += 1
                elif i == 0:
                    direction = 1
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == n - 1:
                    direction = 0
                    j += 1
                elif j == 0:
                    direction = 0
                    i += 1
                else:
                    j -= 1
                    i += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.findDiagonalOrder(mat))