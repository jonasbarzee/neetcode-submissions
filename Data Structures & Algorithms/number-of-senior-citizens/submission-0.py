class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for case in details:
            if int(case[-4:-2:1]) > 60:
                count += 1
        return count
        