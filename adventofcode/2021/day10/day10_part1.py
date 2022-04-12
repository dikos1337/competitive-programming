with open("input.txt", "r") as f:
    file = f.readlines()
    file = [x.strip() for x in file]

stack = []
open_ = ("[", "(", "{", "<")
closed = ("]", ")", "}", ">")
map_co = {c: o for c, o in zip(closed, open_)}
map_oc = {o: c for o, c in zip(open_, closed)}

wrong = []
for line in file:
    for char in line:
        if char in open_:
            stack.append(char)
            continue

        expected = stack.pop()
        if expected != map_co[char]:
            wrong.append(char)
            print(f"Expected {map_oc[expected]}, but found {char} instead.")
            break

weights = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

wrong = [weights[x] for x in wrong]
print("answer =", sum(wrong))
