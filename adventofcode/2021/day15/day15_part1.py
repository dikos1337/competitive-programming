with open("/home/dikos/code/adventofcode/2021/day15/sample.txt", "r") as f:
    file = f.readlines()
    matrix = [list(map(int, list(x.strip()))) for x in file]


def get_neighbors(y, x, matrix):
    out = []
    dirs = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    )
    for direction in dirs:
        dir_y = y + direction[0]
        dir_x = x + direction[1]

        if 0 <= dir_y < len(matrix) and 0 <= dir_x < len(matrix[0]):
            out.append((dir_y, dir_x))

    return out


def search(matrix, y, x, sum_=0, current_path=[], visited_paths=set(), sums=[]):
    current_path.append((y, x))
    sum_ += matrix[y][x]

    if (y == len(matrix) - 1) and (y == len(matrix[0]) - 1):
        visited_paths.add(tuple(current_path))
        
        sums.append(sum_)
        # return visited_paths
        # return matrix[y][x]
    neighbors = get_neighbors(y, x, matrix)

    for y, x in neighbors:
        if (y, x) not in current_path:
            paths_, sums2 = search(matrix, y, x, sum_, current_path, visited_paths, sums)
            current_path.pop()
            sum_ -= matrix[y][x]

            visited_paths |= paths_
            sums += [sums2]
    return visited_paths, sums


path, sums_ = search(matrix, 0, 0)
print(f"{path=}")
print(f"{sums_=}")

for l in matrix:
    print(*l)
