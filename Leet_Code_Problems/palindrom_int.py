class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        return s==s[::-1]


x=121
sol=Solution()
print(sol.isPalindrome(x))