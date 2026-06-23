class Solution:  
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)

        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            target = -num
            print(target)

            while l < r:
                print(nums[l])
                print(nums[r])

                if nums[l] + nums[r] == target and [nums[l], nums[r], num] not in res:
                    # print(f"appending  {[nums[l], nums[r], num]}")
                    res.append([nums[l], nums[r], num])

                if nums[l] + nums[r] < target:
                    l += 1
                # elif nums[l] + nums[r] > target:
                else:
                    r -= 1
                # else:
                #     l, r = l + 1, r - 1
        return res
