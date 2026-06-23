class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for string in strs: 
            key  = ''
            for letter in sorted(string):
                key += letter

            if key in hashMap:
                hashMap[key].append(string)
            else:
                hashMap[key] = [string]
            

        return [hashMap[key] for key in hashMap]


            


        
