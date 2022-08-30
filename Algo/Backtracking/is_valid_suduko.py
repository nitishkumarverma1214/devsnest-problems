
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        squares = [set() for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if board[i][j] !='.':
                    val = board[i][j]
                    if val in rows[i]:
                        return False
                    rows[i].add(val)
                    if val in cols[j]:
                        return False
                    cols[j].add(val)
                    #calculating the index of the box
                    idx = ((i//3) * 3)+ j//3
                    if val in squares[idx]:
                        return False
                    squares[idx].add(val)
                
                    
            
        return True

def print_board(board):
    for row in board:
        print(*row)
def main():
    board =[[".",".",".",".",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],["9","3",".",".","2",".","4",".","."],[".",".","7",".",".",".","3",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3","4",".",".",".","."],[".",".",".",".",".","3",".",".","."],[".",".",".",".",".","5","2",".","."]]
    print_board(board)
    print(Solution().isValidSudoku(board))
if __name__ == '__main__':
    main()
         