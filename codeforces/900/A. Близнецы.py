n = int(input())


def solver(coins):
    l = len(coins)
    if l == 1:
        return 1
    coins.sort()

    half = sum(coins) / 2
    my_coins = 0

    for i in range(l - 1, -1, -1):
        my_coins += coins[i]
        if my_coins > half:
            return l - i
    return l - i


inp = list(map(int, input().split(" ")))
# print(inp)
answer = solver(inp)
print(answer)
