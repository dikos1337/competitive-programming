from typing import List
from functools import reduce
from collections import Counter


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        cache: dict[frozenset, int] = {}
        answer: list[int] = []
        counter = Counter(nums)
        # print("counter", counter)
        nums = nums[::-1]
        while len(nums):
            # print("nums", nums)
            num = nums.pop()
            # print("num", num)

            for num2 in set(nums):
                cache[frozenset((num, num2))] = abs(num - num2)

            valid_keys: list[frozenset] = []
            for key in cache.keys():
                if num in key:  # num in frozenset
                    valid_keys.append(key)

            # print("valid_keys", valid_keys)
            tmp = []
            for key in valid_keys:
                # print("sadas", list(filter(lambda x: x[0] != num, counter.items())))
                cond = list(filter(lambda x: x[0] != num, counter.items()))
                if len(cond) == 1:
                    for k, v in filter(lambda x: x[0] != num, counter.items()):
                        tmp.append(cache[key] * v)
                else:
                    tmp.append(cache[key])

            # print("tmp", tmp)
            answer.append(sum(tmp))
            # print("answer", answer)
        # print("cache", cache)

        return answer


s = Solution()

assert s.getSumAbsoluteDifferences([2, 3, 5]) == [4, 3, 5]
# print("TEST 1 OK!")

assert s.getSumAbsoluteDifferences([1, 4, 6, 8, 10]) == [24, 15, 13, 15, 21]
# print("TEST 2 OK!")

assert s.getSumAbsoluteDifferences([3, 8, 8, 8]) == [15, 5, 5, 5]
# print("TEST 3 OK!")


# print("OK!")
