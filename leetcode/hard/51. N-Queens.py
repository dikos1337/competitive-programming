from typing import List, Set, Tuple
from functools import lru_cache


def compute_positions_under_attack(
    board, n: int, queen_y: int, queen_x: int
) -> Set[Tuple[int]]:
    # вернить список тюплов x y
    positions = []

    # left
    queen_x_tmp = queen_x
    while queen_x_tmp > 0:
        queen_x_tmp -= 1
        positions += [(queen_y, queen_x_tmp)]

    # right
    queen_x_tmp = queen_x
    while queen_x_tmp < n - 1:
        queen_x_tmp += 1
        positions += [(queen_y, queen_x_tmp)]

    # up
    queen_y_tmp = queen_y
    while queen_y_tmp > 0:
        queen_y_tmp -= 1
        positions += [(queen_y_tmp, queen_x)]

    # down
    queen_y_tmp = queen_y
    while queen_y_tmp < n - 1:
        queen_y_tmp += 1
        positions += [(queen_y_tmp, queen_x)]

    # up left
    queen_y_tmp = queen_y
    queen_x_tmp = queen_x
    while (queen_y_tmp > 0) and (queen_x_tmp > 0):
        queen_y_tmp -= 1
        queen_x_tmp -= 1
        positions += [(queen_y_tmp, queen_x_tmp)]

    # up right
    queen_y_tmp = queen_y
    queen_x_tmp = queen_x
    while (queen_y_tmp > 0) and (queen_x_tmp < n - 1):
        queen_y_tmp -= 1
        queen_x_tmp += 1
        positions += [(queen_y_tmp, queen_x_tmp)]

    # down left
    queen_y_tmp = queen_y
    queen_x_tmp = queen_x
    while (queen_y_tmp < n - 1) and (queen_x_tmp > 0):
        queen_y_tmp += 1
        queen_x_tmp -= 1
        positions += [(queen_y_tmp, queen_x_tmp)]

    # down right
    queen_y_tmp = queen_y
    queen_x_tmp = queen_x
    while (queen_y_tmp < n - 1) and (queen_x_tmp < n - 1):
        queen_y_tmp += 1
        queen_x_tmp += 1
        positions += [(queen_y_tmp, queen_x_tmp)]

    return set(positions)


def check_available_positions(board, n: int) -> Set[Tuple[int]]:
    positions_under_attack = set()
    all_positions = set()

    for y in range(n):
        for x in range(n):
            all_positions |= {(y, x)}
            if board[y][x] == "Q":
                positions_under_attack |= compute_positions_under_attack(board, n, y, x)

                all_positions -= {(y, x)}

    available_positions = all_positions - positions_under_attack
    return available_positions


# main loop

answer = []
n = 7
board = [["."] * n for _ in range(n)]

visited = set()


def solution(board, n, path=set()) -> Set[int]:
    global visited, answer
    available_positions = check_available_positions(board, n)

    if not available_positions:
        return path

    for y, x in available_positions:
        board[y][x] = "Q"

        next_path = frozenset(path | {(y, x)})
        if next_path not in visited:
            visited |= {next_path}
            possible_answer = solution(board, n, path | {(y, x)})
            if len(possible_answer) == n:
                answer += [possible_answer]

        board[y][x] = "."
    return path


solution(board, n)
print(len(answer))
