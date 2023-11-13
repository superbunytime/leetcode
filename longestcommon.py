# class Solution:
#     def longestCommonPrefix(self, strs):
#         result_str = ""
#         i = 0
#         strSet = set()
#         lowest = min(strs, key=len)
#         # print(type(lowest))
#         for str in strs:
#             i += 1
#             if len(strSet) > i or i == len(lowest):
#                 return result_str
#             # print(str[0:len(lowest)]) # works up to this point
#             strSet.add(str[i])
#             if len(strSet) == len(lowest) and strSet[-1] == lowest[-1]:
#                 return str(lowest)
#             if len(strSet) > i:
#                 return result_str
#             result_str += str(strSet[i])
            # i think that's good. let's stress test this baby.
            # okay what's happening is i'm trying to str() methods but that's a function argument
            # and not actually a method
            # ...or not?? str is an argument, but strs is the argument passed to the function
            # what's going on????
            # str is also declared in the for loop, when it should be changed to something else.

class Solution:
    def longestCommonPrefix(self, v):
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+= first[i]
        return ans

str1 = ["aaa", "bb", "cccc"]
str2 = ["aaaa", "bbbb", "ccccccc"]
str3 = ["help", "blelppl", "glakughgsk"]
str4 = ["help", "helpme", "helpmeplease"]
str5 = ["hooogh", "hh", "hoe"]
str6 = ["blech", "bleck"]

print(Solution.longestCommonPrefix(Solution, str1)) # expected result, ""
print(Solution.longestCommonPrefix(Solution, str2)) # expected result, ""
print(Solution.longestCommonPrefix(Solution, str3)) # expected result, ""
print(Solution.longestCommonPrefix(Solution, str4)) # expected result, "help"
print(Solution.longestCommonPrefix(Solution, str5)) # expected result, "h"
print(Solution.longestCommonPrefix(Solution, str6)) # expected result, "blec"

# class Solution:
#     def longestCommonPrefix(self, v: List[str]) -> str:
#         ans=""
#         v=sorted(v)
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans 

# anyway i'm moving on but here's the best solution; they sort the array lexically like i did
# but only compared each character of the first and last elements
# they only compared for the length of the shortest element, like i did too.
# i was so close to having it.
# they also used a range instead of a plain for loop. i was so close to having it augh.

