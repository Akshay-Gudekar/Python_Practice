class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))


num1=str(12)
num2=str(14)
sol=Solution()
print(sol.multiply(num1,num2))