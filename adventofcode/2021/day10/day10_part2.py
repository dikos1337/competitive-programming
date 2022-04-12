with open("input.txt", "r") as f:
    file = f.readlines()
    file = [x.strip() for x in file]

open_ = ("[", "(", "{", "<")
closed = ("]", ")", "}", ">")
map_co = {c: o for c, o in zip(closed, open_)}
map_oc = {o: c for o, c in zip(open_, closed)}

answer = []
for line in file:
    stack = []
    need_skip = False

    for char in line:
        if char in open_:
            stack.append(char)
            continue

        expected = stack.pop()
        if expected != map_co[char]:
            need_skip = True
            # wrong.append(char)
            # print(f"Expected {map_oc[expected]}, but found {char} instead.")
            break

    if len(stack) and not need_skip:
        closed_brackets = [stack.pop() for _ in range(len(stack))]
        answer.append(closed_brackets)


weights = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

# wrong = [weights[x] for x in wrong]
# print("answer =", sum(wrong))
# print(stack)
answer = ["".join([map_oc[y] for y in x]) for x in answer]


def compute_score(brackets):
    score = 0
    weights = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    for b in brackets:
        score *= 5
        score += weights[b]

    return score


scores = sorted([compute_score(x) for x in answer])
for a in answer:
    print(a, compute_score(a))

print(*scores)
print("final answer =", scores[len(scores) // 2])
# print(answer)
