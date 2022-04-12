a = int(input())
b = int(input())
c = int(input())

l = [a, b, c]
if l[0] == l[1] == 1:
    if l[2] <= 2:
        print(l[0] + l[1] + l[2])
    else:
        print((l[0] + l[1]) * l[2])
elif l[0] == l[2] == 1:
    print(l[0] + l[1] + l[2])
elif l[1] == l[2] == 1:
    if l[0] <= 2:
        print(l[0] + l[1] + l[2])
    else:
        print(l[0] * (l[1] + l[2]))
elif l[2] == 1:
    print(l[0] * (l[1] + l[2]))
elif l[1] == 1:
    if l[0] < l[2]:
        print((l[0] + l[1]) * l[2])
    else:
        print(l[0] * (l[1] + l[2]))
elif l[0] == 1:
    print((l[0] + l[1]) * l[2])
else:
    print((l[0] * l[1] * l[2]))
