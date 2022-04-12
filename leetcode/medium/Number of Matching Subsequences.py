# from typing import List


class Solution:
    def numMatchingSubseq(self, s, words):
        answer = 0
        for word in words:
            # print("WORD", word)
            char_count = 0
            s_index = 0
            for char in word:
                # print("char", char)
                # print(s[s_index:], "char_count", char_count)

                if char not in s[s_index:]:
                    break
                else:
                    char_count += 1
                    # print(s[s_index:], "char_count+1", char_count)
                    idx = s[s_index:].find(char) + 1
                    s_index += idx if idx != 0 else 1

            if char_count == len(word):
                answer += 1
                # print("answer+1", answer)

        # print("answer", answer)
        return answer


s = Solution()

assert s.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]) == 3, "TEST 1"
print("TEST 1 OK!")

assert (
    s.numMatchingSubseq(
        "dsahjpjauf",
        ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"],
    )
    == 2,
    "TEST 2",
)

s.numMatchingSubseq(
    "dsahjpjahsdjksahdjlashdjashldksalkdaauf" * 10000,
    ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"] * 100,
)

print("TEST 2 OK!")
