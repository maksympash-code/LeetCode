class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r] - target
            if s == 0:
                return [l + 1, r + 1]
            elif s < 0:
                l += 1
            else:
                r -= 1
        return []


if __name__ == '__main__':
    s = Solution()
    numbers = [2,3,4]
    target = 6

    print(s.twoSum(numbers, target))