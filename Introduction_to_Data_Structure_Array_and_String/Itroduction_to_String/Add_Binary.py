class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        i, j, carry = len(a) - 1, len(b) - 1, 0

        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(a[i]) - ord('0')
            if j >= 0:
                sum += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1

            if sum > 1:
                carry = 1
            else:
                carry = 0
            res += str(sum % 2)

        if carry != 0:
            res += str(carry)
        return res[::-1]



# class Solution(object): # best method
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         a = int(a, 2)
#         b = int(b, 2)
#         c = a + b
#         return bin(c)[2:]


if __name__ == '__main__':
    s = Solution()
    a = '11'
    b = '1'
    print(s.addBinary(a, b))