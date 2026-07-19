class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Here we will take 3 checks. A horizontal check, a vertical check and a 9x9 check

        #Checking for duplicates in row

        for row in range(9):
            hs_H = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in hs_H:
                    return False
                hs_H.add(board[row][col])

        #Checking for duplicates in column
        
        for row in range(9):
            hs_V = set()
            for col in range(9):
                if board[col][row] == ".":
                    continue
                if board[col][row] in hs_V:
                    return False
                hs_V.add(board[col][row])
        
        #Checking for duplicates in box
        hs_square = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in hs_square[(row//3,col//3)]:
                    return False
                hs_square[(row//3,col//3)].add(board[row][col])
        return True

        


                

            

