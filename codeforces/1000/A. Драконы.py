s, n = map(int, input().split(" "))

l = []
for _ in range(n):
    dragon_power, bonus = map(int, input().split(" "))
    l.append((dragon_power, bonus))

l.sort(key=lambda x: x[0])

for fight in l:
    if s > fight[0]:
        s += fight[1]
    else:
        print("NO")
        quit()

print("YES")
