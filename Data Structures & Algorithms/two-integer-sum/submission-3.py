class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashMap:
                return [min(i, hashMap[difference]), max(i, hashMap[difference])]
            else:
                hashMap[num] = i
