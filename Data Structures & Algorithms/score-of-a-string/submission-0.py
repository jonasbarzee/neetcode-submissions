class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            first = s[i]
            second = s[i + 1]
            score += abs(ord(second) - ord(first))
        return score

        