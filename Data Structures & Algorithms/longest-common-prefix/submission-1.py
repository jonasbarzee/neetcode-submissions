class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = "" 
        if not strs:
            return prefix

        shortest = strs[0]
        for string in strs: 
            if len(shortest) > len(string):
                shortest = string

        if not shortest:
            return prefix

        for index, character in enumerate(shortest):
            for string in strs:
                if string[index] != character:
                    return prefix
                
            prefix += character

        return prefix



