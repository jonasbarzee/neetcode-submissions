class Solution:  
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            target = -num

            while l < r:


                if nums[l] + nums[r] == target and [nums[l], nums[r], num] not in res:
                    res.append([nums[l], nums[r], num])

                if nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res
