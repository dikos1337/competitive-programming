n = int(input())

l = []
for _ in range(n):
    h, a = map(int, input().split(" "))
    l.append((h, a))

answer = 0
for i in range(n * n):
    if l[i // n][0] == l[i % n][1]:
        # print(f"|| {(i // n)+1}, {(i % n)+1}")
        answer += 1

print(answer)
