from typing import List

with open("input.txt", "r") as f:
    nums = list(map(int, "".join(f.readlines()).strip().split(",")))


init_state = {n: nums.count(n) for n in range(9)}

print(init_state)


def update_state(old_state: List[int]):
    new_state = old_state.copy()

    for i in range(8, -1, -1):
        if i == 0:
            new_state[8] += old_state[0]
            new_state[6] += old_state[0]
            # new_state[0] = 0
        elif i == 8:
            new_state[i - 1] = old_state[i]
            new_state[i] = 0

        elif i > 0:  # i > 0
            new_state[i - 1] = old_state[i]
            # new_state[i] = 0

    # for i, num in enumerate(old_state):
    #     if num > 0:
    #         new_state[i] = num - 1
    #     elif num == 0:
    #         new_state[i] = 6
    #         new_state.append(8)
    return new_state


print("init state:", init_state)
state = init_state.copy()
for i, _ in enumerate(range(256)):
    state = update_state(state)
    print(f"{i = }")
    # print(f"{state = }")

print(f"{state = }")
# answer = len(nums)
answer = sum(state.values())
print(f"{answer = }")
