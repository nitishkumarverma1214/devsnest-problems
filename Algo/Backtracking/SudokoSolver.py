
from typing import List


class Solution:
    def __init__(self):
        self.n = 9
        self.rows = [set() for _ in range(self.n)]
        self.cols = [set() for _ in range(self.n)]
        self.squares = [set() for _ in range(self.n)]
        self.empty_place = []
        
    def isValidSudoku(self, val,r,c) -> bool:
        #calculating the index of the box
        idx = ((r//3) * 3)+ c//3  
        if val in self.rows[r] or val in self.cols[c] or val in self.squares[idx] :
            return False
        return True
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        # mark the already present val in rows, cols and squares list
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] !='.':
                    self.rows[i].add(board[i][j])
                    self.cols[j].add(board[i][j])
                    idx = ((i//3) * 3)+ j//3
                    self.squares[idx].add(board[i][j])
                else:
                    self.empty_place.append((i,j))
        
        curptr = 0
        total_empty = len(self.empty_place)
        prev_val = [0 for _ in range(total_empty)]
        while True:
            
            if curptr == total_empty:
                print(board)
                return 
            for val in range(prev_val[curptr]+1,self.n+1):
                isplaced = False
                r ,c = self.empty_place[curptr]
                isplaced = self.isValidSudoku(str(val),r,c)
                if isplaced:
                    prev_val[curptr] = val 
                    board[r][c] = str(val)
                    self.rows[r].add(str(val))
                    self.cols[c].add(str(val))
                    idx = ((r//3) * 3)+ c//3
                    self.squares[idx].add(str(val))
                    curptr +=1
                    break

            
            if not isplaced:
                
                prev_val[curptr] = 0
                curptr-=1
                # remove the values from cols,rows and squares
                r,c = self.empty_place[curptr]
                pv = str(prev_val[curptr])
                board[r][c] = '.'
                if pv in self.cols[c]:
                    
                    self.cols[c].remove(pv)
                if pv in self.rows[r]:
                    self.rows[r].remove(pv)
                ind = (r//3)*3 + c//3
                if pv in self.squares[ind]:
                    self.squares[ind].remove(pv)

        
        
        

def print_board(board):
    for row in board:
        print(*row)
def main():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # print_board(board)
    Solution().solveSudoku(board)
if __name__ == '__main__':
    main()
         