class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        num = 0
        res = []

        for i in range(n):
            num = num * 10 + digits[i]

        num += 1

        num_string = str(num)
        for i in range(len(num_string)):
            res.append(int(num_string[i]))

        return res


if __name__ == '__main__':
    s = Solution()
    digits = [1, 2, 3]

    result = s.plusOne(digits)
    print(result)