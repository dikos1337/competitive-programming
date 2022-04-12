import statistics

with open("input.txt", "r") as f:
    nums = list(map(int, "".join(f.readlines()).strip().split(",")))

median = int(statistics.median(nums))
answer = sum([abs(num - median) for num in nums])

print(f"{median = } {answer = }")
