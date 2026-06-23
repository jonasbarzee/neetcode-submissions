class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_col = {} 

        for i, row in enumerate(board):
            seen_row = []

            if i == 0 or i == 3 or i == 6:
                seen_box_1 = []
                seen_box_2 = []
                seen_box_3 = []
               

            for j, num in enumerate(row):  
                if num == ".":
                   continue 


                if num in seen_row:
                    return False

                if j in seen_col and num in seen_col[j]: 
                    return False
                
                if j in range(3) and num in seen_box_1:
                    return False

                if j in range(3, 6) and num in seen_box_2:
                    return False

                if j in range(6, 9) and num in seen_box_3:
                    return False
 
                # build row seen
                seen_row.append(num)  

                # build col seen
                if j not in seen_col:
                    seen_col[j] = [num]
                elif j in seen_col:
                    seen_col[j] += [num]
                

                if j in range(3):
                    seen_box_1.append(num)

                if j in range(3, 6):
                    seen_box_2.append(num)
 
                if j in range(6, 9):
                    seen_box_3.append(num)
 
                
                # print(seen_row)
                # print(seen_col)
                # print(seen_box_1)
                # print(seen_box_2)
                # print(seen_box_3)
                
                
        return True

