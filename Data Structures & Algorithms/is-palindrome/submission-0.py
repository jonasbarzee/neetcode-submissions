class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        front = 0
        back = len(s) - 1

        while front != back and front < back:  
            if s[front] != s[back]:
                return False
            
            front += 1
            back -= 1
            
        return True