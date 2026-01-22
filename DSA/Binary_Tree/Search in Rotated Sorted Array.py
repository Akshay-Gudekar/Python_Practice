from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # CONCEPT: Establishing the search boundaries
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # CONCEPT 1: Find the "Normal" (Sorted) Half
            if nums[left] <= nums[mid]:
                # Left side is sorted.

                # CONCEPT 2: Check if target is in this "Normal" range
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is here! Move right boundary.
                else:
                    left = mid + 1  # Target is NOT here! Jump to the other half.

            # CONCEPT 1 (Alternative): Right side must be the "Normal" one
            else:
                # Right side is sorted.

                # CONCEPT 2: Check if target is in this "Normal" range
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target is here! Move left boundary.
                else:
                    right = mid - 1  # Target is NOT here! Jump to the other half.

        return -1


# --- Execution Block ---
if __name__ == "__main__":
    sol = Solution()
    test_array = [4, 5, 6, 7, 0, 1, 2]
    target_val = 0

    result = sol.search(test_array, target_val)

    print(f"Array: {test_array}")
    print(f"Target: {target_val}")
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in array.")


# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1