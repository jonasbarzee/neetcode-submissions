class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def dfs_recursive(self, grid, visited, row, col): 
        if grid[row][col] == "0":
            return
        elif grid[row][col] == "1":
            visited[(row, col)] = True
        
        for row_offset, col_offset in self.DIRECTIONS:
            nr, nc = row + row_offset, col + col_offset
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                self.dfs_recursive(grid, visited, nr, nc) 

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = range(len(grid)), range(len(grid[0]))
        visited = {}
        islands = 0

        for row in ROWS:
            for col in COLS:
                if grid[row][col] == "1" and (row, col) not in visited:
                    self.dfs_recursive(grid, visited, row, col)
                    islands += 1

        return islands
                    

        