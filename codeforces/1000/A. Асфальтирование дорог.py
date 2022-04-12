n = int(input())

done_h = set()
done_v = set()

days = []
for i in range(n * n):
    h, v = map(int, input().split(" "))
    if (h not in done_h) and (v not in done_v):
        done_h.add(h)
        done_v.add(v)
        days.append(i + 1)

print(*days)
