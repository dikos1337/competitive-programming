def solver(a, b):
    a = set(a)
    b = set(b)
    if a.intersection(b) or b.intersection(a):
        return "YES"
    else:
        return "NO"


for _ in range(int(input())):
    a = input()
    b = input()
    answer = solver(a, b)
    print(answer)
