class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        return s==s[::-1]
x=121
sol=Solution()
print(sol.isPalindrome(x)) # 0ms most efficient solution as showed in leetcode

# Find Palindrome With Fixed Length.
class Solution1:
    def kthPalindrome(self, queries: list[int], intLength: int) -> list[int]:
        # 1. Calculate the length of the 'generating' half
        # (intLength + 1) // 2 handles both even and odd lengths
        half_len = (intLength + 1) // 2

        # 2. Smallest half possible (e.g., if half_len is 3, start is 100)
        start_half = 10 ** (half_len - 1)

        # 3. Maximum number of palindromes possible for this length
        # (e.g., for half_len 2, we have 10 to 99, which is 90 total)
        max_palindromes = 9 * start_half

        results = []
        for q in queries:
            if q > max_palindromes:
                results.append(-1)
                continue

            # Construct the half
            current_half = str(start_half + q - 1)

            # Construct the full palindrome
            if intLength % 2 == 0:
                # Even: full half + reversed full half
                res = current_half + current_half[::-1]
            else:
                # Odd: full half + reversed half (excluding the middle character)
                res = current_half + current_half[:-1][::-1]

            results.append(int(res))

        return results


queries = [1,2,3,4,5,90]
intLength = 3
sol1=Solution1()
print(sol1.kthPalindrome(queries,intLength))