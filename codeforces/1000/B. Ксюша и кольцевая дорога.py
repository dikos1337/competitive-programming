n, m = map(int, input().split(" "))
l = map(int, input().split(" "))

times = 0
my_pos = 1

for target_home in l:
    if my_pos <= target_home:
        step = (target_home) - my_pos
    else:
        step = n - (my_pos - target_home)

    times += step
    my_pos += step
    if my_pos > n:
        my_pos = my_pos % n

print(times)
