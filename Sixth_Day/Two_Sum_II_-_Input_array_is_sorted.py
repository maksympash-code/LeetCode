class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0
        right = n - 1

        for i in range(n):
            sums = numbers[left] + numbers[right] - target

            if sums == 0:
                return [left + 1, right + 1]
            elif sums < 0:
                left += 1
            else:
                right -= 1
        return []


if __name__ == '__main__':
    s = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(numbers, target))