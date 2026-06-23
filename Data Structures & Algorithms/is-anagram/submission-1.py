class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [l for l in s]
        t = [l for l in t]
        return sorted(s) == sorted(t)