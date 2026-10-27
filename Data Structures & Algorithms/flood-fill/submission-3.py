class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)] # right, left, down, up
    def dfs(self, image: List[List[int]], row: int, col: int, color: int, starting_color: int):
        image[row][col] = color

        for row_offset, col_offset in self.DIRECTIONS:
            nr, nc = row + row_offset, col + col_offset
            if nr in range(len(image)) and nc in range(len(image[0])) and image[nr][nc] == starting_color:
                self.dfs(image, nr, nc, color, starting_color)  

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc] 
        if starting_color == color:
            return image

        self.dfs(image, sr, sc, color, starting_color)
        return image