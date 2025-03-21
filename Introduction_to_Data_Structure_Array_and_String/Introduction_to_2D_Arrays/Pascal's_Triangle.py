class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for i in range(numRows):
            # Кожен рядок має (i+1) елемент, і починається та закінчується 1
            row = [1] * (i + 1)

            # Обчислюємо внутрішні елементи (якщо i > 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle



if __name__ == '__main__':
    s = Solution()
    numRows = 5

    res = s.generate(numRows)
    print(res)