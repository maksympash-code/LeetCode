class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)
        res = set()

        if n < m:
            nums1.sort()

            for i in range(m):
                l = 0
                r = n - 1

                while l <= r:
                    mid = l + (r - l) // 2
                    if nums1[mid] == nums2[i]:
                        res.add(nums2[i])
                        break
                    elif nums1[mid] < nums2[i]:
                        l = mid + 1
                    else:
                        r = mid - 1


        else:
            nums2.sort()
            for i in range(n):
                l = 0
                r = m - 1

                while l <= r:
                    mid = l + (r - l) // 2
                    if nums2[mid] == nums1[i]:
                        res.add(nums1[i])
                        break
                    elif nums2[mid] < nums1[i]:
                        l = mid + 1
                    else:
                        r = mid - 1

        return list(res)

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(s.intersection(nums1, nums2))