class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summation = 0
        i = 0
        while i < len(nums) + 1:
            summation += i
            i+= 1
        return summation - sum(nums)
        # use summation; subtract the sum of the list from the summation of n: this works in all cases i think
        # use sum method to get the total; that's what you'll be subtracting
        # the more optimal solution is to use XOR, but to quote a senior dev i asked,
        #  "if I ever find you writing code like that in production I will throw all eight pennies of
        # CPU compute time you saved with horribly unreadable code directly at you"