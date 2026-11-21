class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while True:
            if digits[i] == 9 and i == 0:
                digits[i] = 0
                digits.insert(0, 1)
                break
            elif digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
            i -= 1
        return digits
            

            


        