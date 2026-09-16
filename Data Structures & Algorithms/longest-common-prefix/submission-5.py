class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
  
        for index, character in enumerate(strs[0]):
            for string in strs:
                if index == len(string):
                    return strs[0][:max(0, index)] 
                if string[index] != character:
                    return strs[0][:index]
        return strs[0]



