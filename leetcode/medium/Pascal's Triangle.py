from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1 for _ in range(i)] for i in range(1, numRows + 1)]
        if numRows > 1:
            for e, row in enumerate(result):
                for i in range(len(row) - 2):
                    # print("row[i]:", row[i], "row[i + 1]:", row[i + 1])
                    result[e][i + 1] = result[e - 1][i] + result[e - 1][i + 1]
                    # print("row:", row)

        # print("result", result)
        return result


s = Solution()
assert s.generate(1) == [[1]]
assert s.generate(2) == [[1], [1, 1]]
assert s.generate(3) == [[1], [1, 1], [1, 2, 1]]
assert s.generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
assert s.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


print("OK!")
