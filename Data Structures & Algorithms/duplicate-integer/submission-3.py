class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collection = Counter(nums)
        for key in collection:
            if collection[key] >= 2:
                return True
        return False