class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        m = l + (r - l) // 2
        while l <= r:
            m = l + (r - l) // 2 
            found = nums[m]
            if found == target:
                return m
            elif target < found:
                r = m - 1
            elif target > found:
                l = m + 1
        return -1 