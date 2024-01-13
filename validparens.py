class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bababoolean = True
        for i in range(len(s) -1):
            if (s[0] != "("
                or s[0] != "["
                or s[0] != "{"
                or s[-1] != ")"
                or s[-1] != "]"
                or s[-1] != "}"
                or s[i] == "("
                and s[i + 1] != ")"
                or s[i] == "["
                and s[i + 1] != "]"
                or s[i] == "{"
                and s[i + 1] != "}"
            ): # what a fucking mess 
                bababoolean = False
                return bababoolean
        return bababoolean


# test cases

str1 = "(){}[]"
str2 = ")("
str3 = "({[]})"

print(Solution.isValid(Solution, str1))
print(Solution.isValid(Solution, str2))
print(Solution.isValid(Solution, str3))
# so that's fuckin wrong
