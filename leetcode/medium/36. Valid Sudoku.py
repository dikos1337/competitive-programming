from typing import List, Tuple


class Solution:
    def valid_box(self, board: List[List[str]], btcp: Tuple[int]) -> bool:
        cnt = 0
        nums = set()
        for r in (
            (
                board[btcp[0]][btcp[1]],
                board[btcp[0]][btcp[1] + 1],
                board[btcp[0]][btcp[1] + 2],
            ),
            (
                board[btcp[0] + 1][btcp[1]],
                board[btcp[0] + 1][btcp[1] + 1],
                board[btcp[0] + 1][btcp[1] + 2],
            ),
            (
                board[btcp[0] + 2][btcp[1]],
                board[btcp[0] + 2][btcp[1] + 1],
                board[btcp[0] + 2][btcp[1] + 2],
            ),
        ):
            for c in r:
                if c != ".":
                    nums |= {c}
                    cnt += 1

        return len(nums) == cnt

    def valid_row(self, board: List[List[str]], idx: int) -> bool:
        row = board[idx]
        cnt = 0
        nums = set()
        for r in row:
            if r != ".":
                nums |= {r}
                cnt += 1

        return len(nums) == cnt

    def valid_col(self, board: List[List[str]], idx: int) -> bool:
        cnt = 0
        nums = set()
        for r in (
            board[0][idx],
            board[1][idx],
            board[2][idx],
            board[3][idx],
            board[4][idx],
            board[5][idx],
            board[6][idx],
            board[7][idx],
            board[8][idx],
        ):
            if r != ".":
                nums |= {r}
                cnt += 1

        return len(nums) == cnt

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for idx in range(9):
            if not self.valid_col(board, idx):
                return False

        for idx in range(9):
            if not self.valid_row(board, idx):
                return False

        for box_pos in (
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (3, 3),
            (3, 6),
            (6, 0),
            (6, 3),
            (6, 6),
        ):
            if not self.valid_box(board, box_pos):
                return False

        return True


s = Solution()

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
for _ in range(30000):
    assert s.isValidSudoku(board) == True

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
for _ in range(30000):
    assert s.isValidSudoku(board) == False
