class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowset = set()
        column = set()

        for row in board:
            for col in board:
                
                rowset.add(board[row][col])
                column.add(board[row][col])

                if row in rowset:
                    return False
                elif col in column:
                    return False
        return True 
            
