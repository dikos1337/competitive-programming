# with open("sample.txt", "r") as f:
with open("input.txt", "r") as f:
    file = f.readlines()

matrix = [list(map(int, list(x.strip()))) for x in file]


def get_dirs(y, x, matrix):
    out = []
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for direction in dirs:
        dir_y = y + direction[0]
        dir_x = x + direction[1]

        if 0 <= dir_y < len(matrix) and 0 <= dir_x < len(matrix[0]):
            out.append((dir_y, dir_x))

    return out


for line in matrix:
    print(*line)


def search_basin(y: int, x: int, matrix: list[list[int]], mem: set = set()):
    basin_coords = set()
    for dir_y, dir_x in get_dirs(y, x, matrix):
        if (dir_y, dir_x) not in mem:
            if matrix[dir_y][dir_x] != 9:
                basin_coords.add((dir_y, dir_x))
                mem.add((dir_y, dir_x))
                basin_coords |= search_basin(dir_y, dir_x, matrix, mem)

    return frozenset(basin_coords)


basins = set()

for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] != 9:
            basin = search_basin(y, x, matrix)
            if basin != frozenset():
                basins.add(basin)

basins_sizes = sorted([len(x) for x in basins], reverse=True)
answer = basins_sizes[0] * basins_sizes[1] * basins_sizes[2]

print(f"{basins = }")
print(f"{basins_sizes = }")
print(f"{answer = }")
