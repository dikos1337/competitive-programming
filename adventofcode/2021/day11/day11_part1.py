with open("input.txt", "r") as f:
    file = f.readlines()
    matrix = [list(map(int, list(x.strip()))) for x in file]


def get_neighbors(y, x, matrix):
    out = []
    dirs = (
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    )
    for direction in dirs:
        dir_y = y + direction[0]
        dir_x = x + direction[1]

        if 0 <= dir_y < len(matrix) and 0 <= dir_x < len(matrix[0]):
            out.append((dir_y, dir_x))

    return out


def do_flash(y, x, matrix, flashed_this_step):
    neighbors = get_neighbors(y, x, matrix)

    for yy, xx in neighbors:
        if matrix[yy][xx] < 9:
            if (yy, xx) not in flashed_this_step:
                matrix[yy][xx] += 1
        else:
            matrix[yy][xx] = 0
            flashed_this_step.add((yy, xx))
            # print(f"do_flash {y=} {x=} flashed")

            flashed_this_step |= do_flash(yy, xx, matrix, flashed_this_step)
    return flashed_this_step


flash_cnt = 0


def do_step(matrix):
    global flash_cnt
    flashed_this_step = set()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] < 9:
                if (y, x) not in flashed_this_step:
                    matrix[y][x] += 1
            else:
                matrix[y][x] = 0
                flashed_this_step.add((y, x))
                # print(f"do_step {y=} {x=} flashed")

                flashed_this_step |= do_flash(y, x, matrix, flashed_this_step)
                # print_matrix()
    flash_cnt += len(flashed_this_step)
    return matrix


def print_matrix():
    global matrix
    for line in matrix:
        print(line)


for step in range(100):
    print(f"{step+1 = }")
    matrix = do_step(matrix)

    print_matrix()

print(f"{flash_cnt = }")
