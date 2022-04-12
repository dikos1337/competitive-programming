with open("input.txt", "r") as f:
    nums = list(map(int, "".join(f.readlines()).strip().split(",")))

costs = []
for i in range(min(nums), max(nums)):
    cost = [sum(range(1 + abs(x - i))) for x in nums]
    costs.append((i, cost))
    print(f"{i = } of {max(nums) - min(nums)}")


costs.sort(key=lambda x: sum(x[1]))
answer = sum(costs[0][1])
print(f"{answer = }")
