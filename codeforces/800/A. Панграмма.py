from string import ascii_lowercase

n = int(input())
s = input()
if set(s.lower()) == set(ascii_lowercase):
    print("YES")
else:
    print("NO")
