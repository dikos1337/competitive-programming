with open("day1.txt", "r") as f:
    nums = f.read().split("\n")

nums = list(map(int, nums))
# print(nums)

for num in nums:
    nums_copy = nums[:]
    nums_copy.remove(num)
    for num2 in nums_copy:
        nums_copy2 = nums_copy[:]
        for num3 in nums_copy2:

            if num + num2 + num3 == 2020:
                print(num, num2, num3, num * num2 * num3)
