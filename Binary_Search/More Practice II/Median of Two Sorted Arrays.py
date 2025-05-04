class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = half - i

            # Якщо nums1[i] замалий, щоб закрити ліву половину
            if i < m and j > 0 and nums2[j-1] > nums1[i]:
                low = i + 1
            # Якщо nums1[i-1] надто великий
            elif i > 0 and j < n and nums1[i-1] > nums2[j]:
                high = i - 1
            else:
                # Обчислюємо максимум з лівих країв
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])

                # Якщо непарна загальна довжина — повертаємо лівий максимум
                if (m + n) % 2 == 1:
                    return float(max_left)

                # Обчислюємо мінімум з правих країв
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0
        return None