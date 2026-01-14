class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Base Case: If string is empty, there is no palindrome
        if not s or len(s) < 1:
            return ""

        # We store the start and end pointers of the longest palindrome found so far
        start, end = 0, 0

        # We loop through every character in the string to treat it as a 'center'
        for i in range(len(s)):
            # Case 1: Odd length (like "aba"). Center is the character at index i.
            len1 = self.expandAroundCenter(s, i, i)

            # Case 2: Even length (like "abba"). Center is the gap between i and i+1.
            len2 = self.expandAroundCenter(s, i, i + 1)

            # Pick the longer result from the two cases above
            max_len = max(len1, len2)

            # If the palindrome we just found is longer than our previous record:
            if max_len > (end - start):
                # We calculate the new start and end positions.
                # Example: If center i=2 and length is 3 ("aba"),
                # start = 2 - (3-1)//2 = 1. end = 2 + 3//2 = 3.
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        # Return the final substring using slicing (end + 1 because slicing is exclusive)
        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # While pointers are within bounds AND characters match:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # Move outward in both directions
            left -= 1
            right += 1

        # When the loop stops, left and right have moved one step too far.
        # The formula (right - left - 1) calculates the correct length.
        return right - left - 1


if __name__ == "__main__":
    # Create an instance of your class
    sol = Solution()

    # Define a list of random test cases
    test_cases = [
        "babad",  # Expect "bab" or "aba"
        "cbbd",  # Expect "bb"
        "a",  # Expect "a"
        "ac",  # Expect "a" or "c"
        "racecar",  # Expect "racecar"
        "noon",  # Expect "noon"
        "bananas"  # Expect "anana"
    ]

    # Loop through and print results
    print("--- Test Results ---")
    for test in test_cases:
        result = sol.longestPalindrome(test)
        print(f"Input: {test:10} | Result: {result}")