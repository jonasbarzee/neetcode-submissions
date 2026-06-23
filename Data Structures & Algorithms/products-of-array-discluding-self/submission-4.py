class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        res = []

        # [1, 1, 1, 1]
        # [1, 1, 1, 1]

        prev = 1 
        for i in range(len(nums)):
            num = nums[i]
            if i == 0:
                prefix.append(1)
            elif i > 0:
                prefix.append(prev)

            prev *= num

        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if i == len(nums) - 1:
                suffix.append(1)
            elif i < len(nums) - 1:
                suffix.append(prev)
            
            prev *= num
        
        for i in range(len(nums)):
            preIndex = i
            sufIndex = len(nums) - i - 1

            res.append(prefix[preIndex] * suffix[sufIndex])
        
        return res 



            

        