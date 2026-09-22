class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_to_count = {}
        for num in nums:
            if num in nums_to_count:
                nums_to_count[num] += 1
            else:
                nums_to_count[num] = 1

        majority = (0, 0)
        for number, count in nums_to_count.items():
            if count > majority[1]:
                majority = (number, count)

        return majority[0]
