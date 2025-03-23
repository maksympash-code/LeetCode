class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        triangle = []

        for i in range(rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)
        return triangle[rowIndex]



if __name__ == '__main__':
    s = Solution()
    rowIndex = 3
    print(s.getRow(rowIndex))