from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Create the unique list
        unique_elements = sorted(set(nums))
        
        # Overwrite the original list 'nums' in-place
        for i in range(len(unique_elements)):
            nums[i] = unique_elements[i]
        
        # Return the length
        return len(unique_elements)

# --- TESTING ---
sol = Solution()
print("Test 1:", sol.removeDuplicates([1, 1, 2]))             # Result: 2
print("Test 2:", sol.removeDuplicates([1, 1, 2, 2, 3, 3, 4])) # Result: 4