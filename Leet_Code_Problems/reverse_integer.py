

class Solution:
    def reverse(self,x:int)->int:
        # Below is my logic and it passed 1036/1045 testcases ...
        # a = []
        # for i in str(x):
        #     a.append(i)
        #
        # if a[0]=="-":
        #     return int(a[0] + "".join(a[1:][::-1]))
        # else:
        #     return int("".join(a[::-1]))

        # actual code i used with short method.
        s = str(x)
        if s[0] == '-':
            res = int('-' + s[1:][::-1])
        else:
            res = int(s[::-1])

        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0

sol=Solution()
print(sol.reverse(120))


