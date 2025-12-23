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
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1. Create a dictionary to store numbers we've already seen.
        #    The number will be the KEY, and its index will be the VALUE.
        seen_numbers = {}

        # 2. Use 'enumerate' to get both the index (i) and the value (num)
        for i, num in enumerate(nums):
            
            # 3. Calculate the "complement" (the number needed to reach the target)
            complement = target - num
            
            # 4. Check if this complement is already in our dictionary
            if complement in seen_numbers:
                # If found, return the index of the complement and the current index
                return [seen_numbers[complement], i]
            
            # 5. If not found, add the current number and its index to the dictionary
            #    so we can check it against future numbers in the loop.
            seen_numbers[num] = i

        # Return an empty list if no solution is found (though the problem 
        # usually guarantees one solution).
        return []

# --- Example of how to run this locally ---

# Define the input data
nums_list = [2, 7, 11, 15]
target_value = 9

# Create an 'instance' of the Solution class
sol = Solution()

# Call the function and store the result
result = sol.twoSum(nums_list, target_value)

# Print the final answer
print("The indices are:", result)


