class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res = n ^ res
            # easy programming challenge
            # calls for bit manipulation
            # yeah okay leetcode cool ig
        return res