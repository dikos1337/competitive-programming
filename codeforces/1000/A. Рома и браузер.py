n, k = map(int, input().split(" "))
l = list(map(int, input().split(" ")))

res = 0

for b in range(k):
    count = 0
    for c in range(n):
        if b != c % k:
            count += l[c]
    res = max(res, abs(count))

print(res)
