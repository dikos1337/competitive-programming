class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def minCut(self, s: str) -> int:
        if len(s) == 1:
            return 0

        cuts = 0
        max_cuts = 0

        i2 = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                continue
            else:
                print("cut", s[i2:i+1])
                i2 = i+1


        return cuts


sol = Solution()


# s = "a"
# assert sol.minCut(s) == 0

# s = "aaaaa"
# assert sol.minCut(s) == 0

# s = "aab"
# assert sol.minCut(s) == 1

# s = "ab"
# assert sol.minCut(s) == 1

s = "aabbccddee"
# assert 
# sol.minCut(s) == 4

s = "aabbaccecbzzzzcdee"
sol.minCut(s)