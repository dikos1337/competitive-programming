def solver(s, t):
    global len_st

    indexes = []
    for i in range(len_st):
        if s[i] != t[i]:
            indexes.append(i)
            if len(indexes) > 2:
                return "No"

    if len(indexes) == 2:
        if s[indexes[0]] == s[indexes[1]]:
            if t[indexes[0]] == t[indexes[1]]:
                return "Yes"

    return "No"


for test_case in range(int(input())):
    len_st = int(input())
    s = input()
    t = input()
    answer = solver(s, t)
    print(answer)
