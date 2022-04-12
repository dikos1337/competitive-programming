# with open("sample.txt", "r") as f:
with open("input.txt", "r") as f:
    file = f.readlines()

matrix = [list(map(int, list(x.strip()))) for x in file]

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

answer = 0
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        cnt = [True]
        out = []
        for direction in dirs:
            dir_y = y + direction[0]
            dir_x = x + direction[1]

            if 0 <= dir_y < len(matrix) and 0 <= dir_x < len(matrix[0]):
                out.append((dir_y, dir_x))
            for dir_y, dir_x in out:
                if matrix[dir_y][dir_x] <= matrix[y][x]:
                    cnt += [False]
        if all(cnt):
            print(f"{y=} {x=} |", matrix[y][x])
            answer += matrix[y][x] + 1

for line in matrix:
    print(*line)

print("answer: ", answer)

# print(answer)
print(len(matrix), len(matrix[0]))
