class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)] # right, left, down, up 
        height, width = len(image), len(image[0])
        starting_color = image[sr][sc]
        if starting_color == color: 
            return image

        to_visit = [(sr,sc)]
        while to_visit:
            row, col = to_visit.pop(0) 
            image[row][col] = color

            for delta_row,delta_col in DIRECTIONS:
                new_row, new_col = row + delta_row, col + delta_col
                if new_row in range(height) and new_col in range(width) and image[new_row][new_col] == starting_color: 
                    to_visit.append((new_row, new_col))   

        return image

        