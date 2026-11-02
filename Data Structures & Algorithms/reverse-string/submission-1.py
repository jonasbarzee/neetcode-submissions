class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n == 1:
            return

        if n & 1: # odd length
            mid = n // 2
            counter = 1
            while counter < mid + 1:
                l,r = mid-counter, mid+counter
                tmp = s[l]
                s[l] = s[r]
                s[r] = tmp 
                counter += 1
        
        else: # even length
            l_mid, r_mid = (n // 2) - 1, n // 2
            while l_mid >= 0 and r_mid <= n -1:
                print(l_mid, r_mid)
                tmp = s[l_mid]
                s[l_mid] = s[r_mid]
                s[r_mid] = tmp
                l_mid -= 1
                r_mid += 1 

        