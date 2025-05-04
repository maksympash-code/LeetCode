class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)
        l = 0
        r = n  - k

        while l < r:
            mid = l + (r - l) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l: l + k]

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5]
    print(s.findClosestElements(nums, 4, 3))