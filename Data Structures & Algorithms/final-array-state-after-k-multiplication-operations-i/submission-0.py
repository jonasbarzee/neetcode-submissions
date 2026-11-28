class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min = float("inf")
            min_idx = None
            for i, num in enumerate(nums):
                if min > num:
                    min = num
                    min_idx = i
            nums[min_idx] *= multiplier

        return nums
        