from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

            # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Check this character against all other strings
            for j in range(1, len(strs)):
                # If we reached the end of a string or characters don't match
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]

        return strs[0]
    # Below is the alternate method to solve this code.
    # def longestCommonPrefix(strs):
    #     if not strs:
    #         return ""
    #
    #     # Sort the strings alphabetically
    #     strs.sort()
    #
    #     first = strs[0]
    #     last = strs[-1]
    #     i = 0
    #
    #     # Only compare the first and the last string
    #     while i < len(first) and i < len(last) and first[i] == last[i]:
    #         i += 1
    #
    #     return first[:i]








strs = ["flower","flow","flight"]
sol=Solution()
print(sol.longestCommonPrefix(strs))