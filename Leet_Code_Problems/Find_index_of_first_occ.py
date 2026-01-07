class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 1. Get the lengths of both strings
        n = len(haystack)
        m = len(needle)

        # 2. Edge case: If needle is longer than haystack, it can't exist inside it
        if m > n:
            return -1

        # 3. Iterate through the haystack
        # We only need to go up to (n - m + 1) because a needle of length 'm'
        # cannot start later than that index.
        for i in range(n - m + 1):

            # 4. Check if the slice of haystack matches the needle
            # haystack[i : i + m] takes a 'window' of size m starting at index i
            if haystack[i: i + m] == needle:
                return i  # Return the first occurrence index immediately

        # 5. If the loop finishes without returning, the needle wasn't found
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(f"Result 1: {sol.strStr('sadbutsad', 'sad')}")  # Expected: 0
    print(f"Result 2: {sol.strStr('leetcode', 'leeto')}")  # Expected: -1