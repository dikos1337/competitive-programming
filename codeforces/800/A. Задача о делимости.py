def solution(a, b):
    if a % b != 0:
        return b - a % b
    else:
        return 0


t = int(input())

for _ in range(t):
    a, b = map(int, input().split(" "))
    answer = solution(a, b)
    print(answer)

# assert solution(10, 4) == 2
# assert solution(13, 9) == 5
# assert solution(100, 13) == 4
# assert solution(123, 456) == 333
# assert solution(92, 46) == 0
# assert solution(877914575, 158260522) == 71648557
# print("OK!")
