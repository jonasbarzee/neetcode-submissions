class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n, total = len(nums), sum(nums)
        return (n * (n + 1) // 2) - total
        