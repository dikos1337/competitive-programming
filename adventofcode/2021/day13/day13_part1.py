# with open("sample.txt", "r") as f:
with open("input.txt", "r") as f:
    file = f.readlines()
    file = [x.strip() for x in file]

i = file.index("")
coordinates = file[:i]


x_max = 0
y_max = 0

for coordinate in coordinates:
    x, y = map(int, coordinate.split(","))
    if x > x_max:
        x_max = x
    if y > y_max:
        y_max = y

matrix = [["." for _ in range(x_max + 1)] for _ in range(y_max + 1)]


# INIT MATRIX
for coordinate in coordinates:
    x, y = map(int, coordinate.split(","))
    matrix[y][x] = "#"

# for line in matrix:
#     print(*line)


def print_fold_line(matrix, fold_along, by):
    if by == "y":
        print(by, fold_along, "".join(matrix[fold_along]))
        print("\n-----")
    if by == "x":
        print(by, fold_along, end=" ")
        for row in matrix:
            print(row[fold_along], end="")
        print("\n-----")


def fold_by_y(matrix, fold_along):
    y_max = len(matrix) - 1
    x_max = len(matrix[0]) - 1
    for bottom_y in range(y_max, fold_along - 1, -1):
        # print(f"{bottom_y - fold_along = }")

        # print(f"{y_max - bottom_y = }", f"{bottom_y = }")
        # print(f"{fold_along + y_max - bottom_y = }")
        # print(f"{fold_along + y_max - bottom_y } {bottom_y - fold_along}")

        # print(f"{y_max - bottom_y} {bottom_y}", "TRUE")

        for bottom_x in range(x_max + 1):
            # if matrix[bottom_y][bottom_x] == "#":
            #     matrix[y_max - bottom_y][bottom_x] = matrix[bottom_y][bottom_x]

            if matrix[fold_along + y_max - bottom_y][bottom_x] == "#":
                matrix[bottom_y - fold_along][bottom_x] = matrix[fold_along + y_max - bottom_y][bottom_x]
            #     matrix[fold_along + y_max - bottom_y][bottom_x] = matrix[bottom_y - fold_along][bottom_x]

    matrix = matrix[:bottom_y]
    return matrix


def fold_by_x(matrix, fold_along):
    y_max = len(matrix) - 1
    x_max = len(matrix[0]) - 1
    for right_y in range(y_max + 1):
        for right_x in range(x_max, fold_along - 1, -1):
            # print(f"{right_x - fold_along} {fold_along + x_max - right_x }")

            # print(f"{x_max - right_x} {right_x}", "TRUE")

            # if matrix[right_y][right_x] == "#":
            #     matrix[right_y][x_max - right_x] = matrix[right_y][right_x]
            if matrix[right_y][fold_along + x_max - right_x] == "#":
                matrix[right_y][right_x - fold_along] = matrix[right_y][fold_along + x_max - right_x]

    matrix = [matrix[y][:right_x] for y in range(y_max + 1)]
    return matrix


for line in file[i + 1 :][:1]:
    if "y=" in line:
        fold_along = int(line.split("=")[1])
        print_fold_line(matrix, fold_along, "y")
        matrix = fold_by_y(matrix, fold_along)
    elif "x=" in line:
        fold_along = int(line.split("=")[1])
        print_fold_line(matrix, fold_along, "x")
        matrix = fold_by_x(matrix, fold_along)


for line in matrix:
    print("".join(line))
# print(*line)

answer = [x.count("#") for x in matrix]
print(sum(answer))

y_max = len(matrix) - 1
x_max = len(matrix[0]) - 1

print(f"{x_max=} {y_max=}")
