from typing import List


class Solution:
    def isValid(self,row,col,board_row):
        # here i denotes the row and board_row[i] denotes the col in which queen of i th row is placed.
        for i in range(len(board_row)):
            # 1. condition is when two queen are placed in same col
            # 2. condition is when the difference of x co-ordinates are equal to difference of y- co-ordinate
            # i.e when queen is placed at diagonal.
            if col== board_row[i] or (row-i) == abs(col - board_row[i] ):
                return False 
        return True

    def solveNQueens(self,n:int)->List[List[str]]:
        board= [['.']*n for _ in range(n)]
        res = []
        # board_row[i] stores the col position of i th row queen
        board_row = [-1]*n
        
        cur_row = 0
        while cur_row != -1 :
            isQueenPlaced = False 
            

            for col in range(board_row[cur_row]+1,n):
                isQueenPlaced = self.isValid(cur_row,col,board_row)
                if isQueenPlaced:
                    board_row[cur_row] = col 
                    board[cur_row][col] = 'Q'
                    cur_row+=1
                    break 
                
            if cur_row == n:
                res.append([''.join(x) for x in board])
                board[cur_row-1][board_row[cur_row-1]]='.'
                board[cur_row-2][board_row[cur_row-2]]='.'
                board_row[-1] = -1
                cur_row -=2
            
            if not isQueenPlaced:
                if  board_row[cur_row] !=-1:
                    board[cur_row][board_row[cur_row]] = '.'
                board_row[cur_row] = -1
                
                cur_row-=1
                board[cur_row][board_row[cur_row]] = '.'
        
        return res

def main():
    print(Solution().solveNQueens(6))   
if __name__ == '__main__':
    main()