# each row and col contains digits 1-9 without repeating
# each box contains digits 1-9 without repeating
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])
        return True