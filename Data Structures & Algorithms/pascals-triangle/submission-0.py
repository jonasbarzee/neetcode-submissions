class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        while numRows -1:
            next = [1]
            if len(res[-1]) != 1:
                for i in range(len(res[-1]) - 1):
                    next.append(res[-1][i] + res[-1][i+1])
                next.append(1) 
                res.append(next)
            else:
                res.append([1, 1])    
            numRows -= 1
        return res