from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        intersection = set(nums1).intersection(set(nums2))
        result = []
        for value in intersection:
            for _ in range(min(c1[value], c2[value])):
                result.append(value)
        return result


s = Solution()

assert s.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
print("TEST 1 OK!")

assert s.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9] or [9, 4]
print("OK!")
