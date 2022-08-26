def printMaze(maze):
    for row in maze:
        print(*row)


def findMinPath():
    a_pos = b_pos = None 
    floor = '.'
    wall = '#'
    start ='A'
    end = 'B'
    path = []

    maze = [['#','#','#','#','#','#','#','#'],['#','.','A','#','.','.','.','#',],['#','.','#','#','.','#','B','#',],['#','.','.','.','.','.','.','#'],['#','#','#','#','#','#','#','#']]
    n,m = len(maze),len(maze[0])
    printMaze(maze)
    for i in range(n):
        for j in range(m):
            if maze[i][j] ==start:
                a_pos = (i,j)
            if maze[i][j] == end:
                b_pos = (i,j)
        if a_pos and b_pos:
            break


    def dfs(r,c):
        if (r,c) == end:
            return 
        Dir = [0,1,0,-1,0]
        for i in range(4):
            nr = r+Dir[i]
            nc = c+Dir[i+1]
            if 0<=nr<n and 0<=nc<m and maze[nr][nc]!=wall:
                
                dfs(nr,nc)



    dfs(a_pos)



def main():
    findMinPath()
    
if __name__ == '__main__':
    main()