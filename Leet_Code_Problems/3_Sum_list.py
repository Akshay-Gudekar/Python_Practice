
class Solution:
    def three_sum(self, nums):
        # 1. Sort the input list. This is crucial for the two-pointer technique
        # and for easily skipping duplicate numbers.
        nums.sort()

        # 2. Initialize an empty list to store our result triplets.
        results = []

        # 3. Start a loop to pick the 'first' number of our triplet (nums[i]).
        # We stop 2 elements before the end because we need space for 'left' and 'right'.
        for i in range(len(nums) - 2):

            # 4. If the current number is the same as the previous one, skip it.
            # This prevents us from generating the same triplet twice.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 5. Initialize two pointers:
            # 'left' starts just after the first number.
            # 'right' starts at the very end of the sorted list.
            left = i + 1
            right = len(nums) - 1

            # 6. While the pointers haven't met, check the sum.
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # 7. If the sum is zero, we found a valid triplet!
                if current_sum == 0:
                    results.append([nums[i], nums[left], nums[right]])

                    # 8. Move the 'left' pointer forward past any duplicate numbers.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # 9. Move the 'right' pointer backward past any duplicate numbers.
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 10. Move both pointers inward to look for the next possible pair.
                    left += 1
                    right -= 1

                # 11. If the sum is too small (less than 0), we need a bigger number.
                # Since the list is sorted, moving 'left' to the right increases the sum.
                elif current_sum < 0:
                    left += 1

                # 12. If the sum is too big (greater than 0), we need a smaller number.
                # Moving 'right' to the left decreases the sum.
                else:
                    right -= 1

        return results

    #Below is My Appraoch
    def three_sum_brute_force(self, nums):
        # We need at least 3 numbers to find a triplet
        if len(nums) < 3:
            return []

        output = []
        n = len(nums)

        # First loop: picks the first element
        for i in range(n):
            # Second loop: picks the second element (starts after i)
            for j in range(i + 1, n):
                # Third loop: picks the third element (starts after j)
                for k in range(j + 1, n):
                    # Check if the values at these three positions sum to zero
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        # Ensure we don't add the same triplet values twice
                        if triplet not in output:
                            output.append(triplet)

        return output

# --- PyCharm Execution Block ---
# This part allows you to run the script directly to see the output.
if __name__ == "__main__":
    test_input = [-1, 0, 1, 2, -1, -4]
    print(f"Input List: {test_input}")

    # Call the function and store the result
    sol=Solution()


    print(f"Unique triplets that sum to zero: {sol.three_sum(test_input)}")
    print(f"Unique triplets that sum to zero: {sol.three_sum_brute_force(test_input)}")