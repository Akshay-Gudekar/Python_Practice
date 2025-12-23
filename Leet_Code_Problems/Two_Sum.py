# My logic
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]


Sol=Solution()
result=print(Sol.twoSum(nums=[2,4,5,6,7],target=9))

# Efficient Logic

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):  #use enum so that we will get index value and value in dict{key:value}
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


