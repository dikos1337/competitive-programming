# https://codeforces.com/problemset/problem/318/A?locale=ru


# n, n2 = 1000000000000, 500000000001 #map(int, input().split(" "))
n, n2 = map(int, input().split(" "))

evens = []
odds = []

for num in range(1, n + 1):
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

odds.extend(evens)


print(odds[n2 - 1])
