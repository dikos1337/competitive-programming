def solver(n):
    if n <= 9:
        return n
    answer = 9
    m = 11
    mul = 10
    i = 0
    while m <= n:
        for i in range(1, 10):
            if m * i <= n:
                answer += 1

        mul *= 10
        m += mul

    return answer


for _ in range(int(input())):
    num = int(input())
    answer = solver(num)
    print(answer)
