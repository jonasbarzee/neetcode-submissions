class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)] # down, up, right, left
        ROWS, COLS = len(grid), len(grid[0])
        visited = {}
        islands = 0

        def dfs(row, col):
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()

                for row_off, col_off in DIRECTIONS:
                    nr, nc = row + row_off, col + col_off
                    if (nr, nc) not in visited and nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "1":
                        stack.append((nr, nc)) 

                visited[(row, col)] = True

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col) 
                    islands += 1
        
        return islands