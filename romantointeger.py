import random

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
         

Solution.romanGenerator()



# tests

rom1 = ""

# notes

# so i think how to solve this is i want to have a large if chain
# that handles prefix numbers (ie: IX, IV, etc) first.
# only the I's following a number have meaning as 1's.
# wait is that right?
# other letters prefixing can do the same thing I's can, i forgot.
# that complicates things.
# it would be extraneous, but i could write a helper function
# to generate valid test cases.
# my brain isn't thinking correctly right now
