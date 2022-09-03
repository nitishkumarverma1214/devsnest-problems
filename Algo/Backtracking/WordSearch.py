from typing import List
class Solution:
     
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        def search_word(r,c,pos):

            if pos==len(word):
                return True
            temp = board[r][c]
            board[r][c] = '#'
            Dir = [0,1,0,-1,0]
            for i in range(4):
                nr = r+Dir[i] 
                nc = c+Dir[i+1]
                if 0<=nr<m and 0<=nc<n and board[nr][nc] == word[pos]:
                    if search_word(nr,nc,pos+1,):
                        return True

            board[r][c] = temp
            return False

        for i in range(m):
                for j in range(n):
                    
                    if board[i][j] == word[0]:
                        
                        if search_word(i,j,pos=1):
                            return True  

        return False 
               
        
def print_board(board):
    for row in board:
        print(*row)
def main():
    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word = "AAB"
    print_board(board)
    print(Solution().exist(board,word))   
if __name__ == '__main__':
    main()