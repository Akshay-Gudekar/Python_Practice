class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. Use a set to store unique characters in the current window
        char_set = set()

        # 2. 'left' pointer for the start of the window
        left = 0
        max_length = 0

        # 3. 'right' pointer iterates through the string
        for right in range(len(s)):

            # 4. If the character is already in the set, it's a duplicate.
            # We must move the left pointer and remove characters until
            # the duplicate is gone.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # 5. Add the current character to the set
            char_set.add(s[right])

            # 6. Calculate the current window size (right - left + 1)
            # and update max_length if this window is bigger.
            max_length = max(max_length, right - left + 1)

        return max_length


s="abcabcbb"
sol=Solution()
print(sol.lengthOfLongestSubstring(s))
