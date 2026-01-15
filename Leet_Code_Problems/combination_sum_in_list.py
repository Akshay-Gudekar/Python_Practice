from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Create a list of 'buckets' from 0 to target
        # dp[i] will store all combinations that sum to i
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]  # Base case: to get 0, you use nothing

        for c in candidates:
            for i in range(c, target + 1):
                # For every combination that already makes (i - c)
                # add the current candidate 'c' to it to make 'i'
                for combo in dp[i - c]:
                    dp[i].append(combo + [c])

        return dp[target]




if __name__ == '__main__':
    sol=Solution()
    print(sol.combinationSum([2,3,6,7],7))


# Below example is using backtracking
# from typing import List
#
#
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         results = []
#
#         def backtrack(remaining, combo, start_index):
#             # Base Case 1: We hit the target exactly
#             if remaining == 0:
#                 results.append(list(combo))
#                 return
#
#             # Base Case 2: We exceeded the target (Stop searching this path)
#             if remaining < 0:
#                 return
#
#             for i in range(start_index, len(candidates)):
#                 # 1. Choose the number
#                 combo.append(candidates[i])
#
#                 # 2. Explore: Call the function again with the NEW remaining sum
#                 # Note: we stay at index 'i' because we can reuse the same number
#                 backtrack(remaining - candidates[i], combo, i)
#
#                 # 3. Backtrack: Remove the number so we can try the next candidate
#                 combo.pop()
#
#         backtrack(target, [], 0)
#         return results
#
#
# # How to run in PyCharm:
# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.combinationSum([2, 3, 6, 7], 7))
#     # Output: [[2, 2, 3], [7]]