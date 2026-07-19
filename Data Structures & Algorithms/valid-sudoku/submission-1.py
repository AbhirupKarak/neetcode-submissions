class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Here we will take 3 checks. A horizontal check, a vertical check and a 9x9 check

        #Checking for duplicates in row

        hs_V = defaultdict(set)
        hs_sq = defaultdict(set)
        for row in range(9):
            hs_H = set()
            for col in range(9):
                if board[row][col] == "." or board[row][col] == ".":
                    continue
                
                if board[row][col] in hs_H:
                    return False
                hs_H.add(board[row][col])

                if board[row][col] in hs_V[col]:
                    return False
                hs_V[col].add(board[row][col])

                if board[row][col] in hs_sq[(row//3, col//3)]:
                    return False
                hs_sq[(row//3, col//3)].add(board[row][col])
            
        return True


                



        


                

            

