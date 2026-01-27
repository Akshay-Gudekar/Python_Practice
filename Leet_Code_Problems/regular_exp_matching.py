class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Cache to store results: (index_in_s, index_in_p) -> True/False
        memo = {}

        def dfs(i, j):
            # Check if we already calculated this
            if (i, j) in memo:
                return memo[(i, j)]

            # Base Case: If we reached the end of the pattern
            if j == len(p):
                return i == len(s)

            # Check if the first characters match
            # (i < len(s) ensures we haven't run out of string)
            first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # Handle the '*' Wildcard
            if (j + 1) < len(p) and p[j + 1] == "*":
                # Option 1: Skip the '*' (use zero of the preceding character)
                # Option 2: Use the '*' (if first_match is true, move string pointer i)
                res = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
                memo[(i, j)] = res
                return res

            # No '*', just move both pointers if they match
            if first_match:
                res = dfs(i + 1, j + 1)
                memo[(i, j)] = res
                return res

            # No match
            memo[(i, j)] = False
            return False

        return dfs(0, 0)

# --- Testing in PyCharm ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Match 'aa' with 'a*': {sol.isMatch('aa', 'a*')}")    # True
    print(f"Match 'mississippi' with 'mis*is*p*.': {sol.isMatch('mississippi', 'mis*is*p*.')}") # False