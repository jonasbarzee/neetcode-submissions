class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        strs = sorted(strs, key=len) 
        shortest = strs[0]
        if not shortest:
            return ""

        prefix = ""   
        
        for index, character in enumerate(shortest):
            for string in strs:
                if string[index] != character:
                    return prefix
                
            prefix += character

        return prefix



