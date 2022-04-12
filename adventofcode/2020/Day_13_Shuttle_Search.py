input_data = """1000417
23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,479,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19""".split(
    "\n"
)


print(input_data)
min_time = int(input_data[0])
print(min_time)
buses = list(map(int, filter(lambda x: x != "x", input_data[1].split(","))))
print(buses)

delta_time = None
bus_num = None
d = []

for bus in buses:
    for i in range(0, min_time * 2, bus):
        # print(i, min_time)
        if i >= min_time:
            delta_time = i - min_time
            bus_num = bus
            d.append((i, delta_time, bus_num))
            break
    print("result:", delta_time * bus_num, f"{bus_num = } {delta_time = }")

answ = list(sorted(d, key=lambda x: x[0]))

print(answ)
print(answ[0][1] * answ[0][2])
