from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1. Convert list [1, 2, 9] -> string "129"
        s = "".join(map(str, digits))

        # 2. Convert string "129" -> int 129, then add 1 -> 130
        num = int(s) + 1

        # 3. Convert int 130 back to list [1, 3, 0]
        return [int(d) for d in str(num)]


digits = [9]
sol = Solution()
print(sol.plusOne(digits))  # Output: [1, 0]