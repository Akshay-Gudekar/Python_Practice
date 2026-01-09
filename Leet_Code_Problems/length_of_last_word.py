class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split() #if we wanted to split by anything then only mention in "" quote
        return len(string[-1])



sol=Solution()
print(sol.lengthOfLastWord("Hello World"))