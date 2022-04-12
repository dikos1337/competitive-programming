from typing import List

with open("input.txt", "r") as f:
    nums = list(map(int, "".join(f.readlines()).strip().split(",")))


def update_state(old_state: List[int]):
    new_state = old_state.copy()

    for i, num in enumerate(old_state):
        if num > 0:
            new_state[i] = num - 1
        elif num == 0:
            new_state[i] = 6
            new_state.append(8)
    return new_state


print("init nums:", nums)
for i, _ in enumerate(range(80)):
    nums = update_state(nums)
    # print(f"{i = }")

answer = len(nums)
print(f"{answer = }")
