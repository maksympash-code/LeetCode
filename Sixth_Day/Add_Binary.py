class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)

        c = a + b

        return bin(c)[2::]


if __name__ == '__main__':
    s = Solution()
    a = '11'
    b = '1'
    res = s.addBinary(a, b)
    print(res)