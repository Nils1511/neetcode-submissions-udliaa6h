class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            duplicate = set()
            for j in range(0, 9):
                if board[i][j] in duplicate:
                    return False
                elif board[i][j] != ".":
                        duplicate.add(board[i][j])
        
        for j in range(0, 9):
            duplicate_col = set()
            for i in range(0, 9):
                if board[i][j] in duplicate_col:
                    return False
                elif board[i][j] != ".":
                        duplicate_col.add(board[i][j])

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                duplicate = set()
                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        if board[i][j] in duplicate:
                            return False
                        elif board[i][j] != ".":
                            duplicate.add(board[i][j])
            
        return True

            

