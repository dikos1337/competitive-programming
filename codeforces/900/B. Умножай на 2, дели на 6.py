n = int(input())


def solver(num):
    if num == 1:
        return 0

    steps = 0
    while num != 1:
        if num % 2 == 0 and num % 6 != 0:
            return -1
        elif num % 6 == 0:
            num /= 6
            steps += 1
        else:
            num *= 2
            steps += 1

    return steps


for _ in range(n):
    t = int(input())

    print(solver(t))
