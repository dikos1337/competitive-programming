class Solution:
    def queryString(self, s: str, n: int) -> bool:
        result = True
        for x in range(1, n + 1):
            if bin(x)[2:] not in s:
                result = False
        return result


s = Solution()

assert s.queryString("0110", 3) == True
assert s.queryString("0110", 4) == False
print("OK!")
