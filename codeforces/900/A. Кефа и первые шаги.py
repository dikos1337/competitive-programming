n = int(input())


def solver(coins):
    steps = 1
    max_steps = 1
    for i in range(len(coins) - 1):
        if coins[i] <= coins[i + 1]:
            steps += 1
            if steps > max_steps:
                max_steps = steps
        else:
            steps = 1

    return max_steps


inp = list(map(int, input().split(" ")))
# print(inp)
answer = solver(inp)
print(answer)
