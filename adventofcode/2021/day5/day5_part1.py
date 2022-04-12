# with open("/home/dikos/code/c/adventofcode/2021/day5/sample.txt", "r") as f:
with open("/home/dikos/code/c/adventofcode/2021/day5/input.txt", "r") as f:

    file = f.readlines()


points = []
x_max = 0
y_max = 0

for line in file:
    # print(line.replace("\n", ""))
    p1, p2 = line.replace("\n", "").split(" -> ")
    x1, y1 = list(map(int, p1.split(",")))
    x2, y2 = list(map(int, p2.split(",")))

    x_max = max([x1, x2, x_max])
    y_max = max([y1, y2, y_max])

    struct = {
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2,
    }

    if (x1 == x2) or (y1 == y2):
        points.append(struct)

print(f"{x_max=} {y_max=}")

field = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]


for p in points:
    print(p)
    if p["x1"] == p["x2"]:
        direction = "y"
    if p["y1"] == p["y2"]:
        direction = "x"

    if direction == "y":
        yma = max([p["y1"], p["y2"]])
        ymi = min([p["y1"], p["y2"]])
        for i in range(ymi, yma + 1):
            field[i][p["x1"]] += 1

    if direction == "x":
        xma = max([p["x1"], p["x2"]])
        xmi = min([p["x1"], p["x2"]])
        for i in range(xmi, xma + 1):
            field[p["y1"]][i] += 1

answer = 0
for line in field:
    for num in line:
        if num >= 2:
            answer += 1

print(f"{answer=}")
