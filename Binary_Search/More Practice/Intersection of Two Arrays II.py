class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)
        res = []

        if n < m:
            nums1.sort()

            for i in range(m):
                l = 0
                r = n - 1

                while l <= r:
                    mid = l + (r - l) // 2
                    if nums1[mid] == nums2[i]:
                        res.append(nums2[i])
                        l = mid + 1
                        break
                    elif nums1[mid] < nums2[i]:
                        l = mid + 1
                    else:
                        r = mid - 1

        else:
            nums2.sort()
            res = []
            for i in range(n):
                l = 0
                r = m - 1

                while l <= r:
                    mid = l + (r - l) // 2
                    if nums2[mid] == nums1[i]:
                        res.append(nums1[i])
                        l = mid + 1
                        break
                    elif nums2[mid] < nums1[i]:
                        l = mid + 1
                    else:
                        r = mid - 1

        return res

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    res = s.intersect(nums1, nums2)
    print(res)