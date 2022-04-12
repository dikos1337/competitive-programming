def solver(a):
    global len_a

    i = 0
    cnt = 0
    while i < len_a:
        cnt += 1
        max_i = a[i]
        while i + 1 < max_i:
            i += 1
            max_i = max(max_i, a[i])

        i += 1

    return cnt


len_a = int(input())
a = tuple(map(int, input().split(" ")))
answer = solver(a)
print(answer)
