class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False 
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for j in range(9):
                if board[col][j] == ".":
                    continue 
                if board[col][i] in seen:
                    return False 
            seen.add(board[col][i])
        
        for sq in range(9):
            seen = set()

            for i in range(3):
                for j in range(3):
                    row = (sq //3) * 3 + i
                    col = (sq //3) * 3 + j

                    if board[row][col] == ".":
                        continue 
                    if board[row][col] in seen:
                        return False 
                    seen.add(board[row][col]) 
        
        return True 
                


            


        
        # cols = collections.defaultdict(set)
        # rows = collections.defaultdict(set)
        # squares = collections.defaultdict(set)# key(row / 3, column / 3)

        # for r in range(9):
        #     for c in range(9):

        #         # skip empty space 
        #         if board[r][c] == ".":
        #             continue 
        #         if (board[r][c] in rows[r] or 
        #             board[r][c] in cols[c] or 
        #             board[r][c] in squares[(r // 3, c //3)]):
        #             return False 
        #         cols[c].add(board[r][c])
        #         rows[r].add(board[r][c])
        #         squares[(r // 3, c //3)].add(board[r][c])
                
        # return True 
                