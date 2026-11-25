class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        result = []
        for i in range(len(words) - 1):
            word = words[i]
            for j in range(i+1, len(words)):
                if word in words[j]:
                    result.append(word)
                    break
        return result
        