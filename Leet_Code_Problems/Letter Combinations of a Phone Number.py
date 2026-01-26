from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 1. Handle the edge case of an empty string
        if not digits:
            return []

        # 2. Define the keypad mapping
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        combinations = []

        # 3. Define the backtracking function
        def backtrack(index: int, current_path: List[str]):
            # If the path is the same length as digits, we are done with this branch
            if len(current_path) == len(digits):
                combinations.append("".join(current_path))
                return

            # Get the letters for the current digit (e.g., "2" -> "abc")
            possible_letters = phone_map[digits[index]]

            for letter in possible_letters:
                # Add the letter and move to the next digit
                current_path.append(letter)
                backtrack(index + 1, current_path)

                # BACKTRACK: Remove the letter so we can try the next one
                current_path.pop()

        # Start the process from the first digit (index 0)
        backtrack(0, [])
        return combinations


# --- Testing in PyCharm ---
if __name__ == "__main__":
    sol = Solution()
    input_digits = "23"
    result = sol.letterCombinations(input_digits)
    print(f"Combinations for '{input_digits}': {result}")
    # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']


# # other logic
# if not digits:
#     return []
#
# phone_map = {
#     "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
#     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
# }

# Initialize results with an empty string to start the "snowball"
# results = [""]
#
# for digit in digits:
#     new_combinations = []
#     # Take the letters for the current digit (e.g., "abc")
#     letters = phone_map[digit]
#
#     # For every combination we have built so far...
#     for combination in results:
#         # ...attach every possible new letter to it
#         for char in letters:
#             new_combinations.append(combination + char)
#
#     # Update results to be the new, longer combinations
#     results = new_combinations
#
# return results