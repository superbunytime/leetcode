class Solution(object):
    def findDisappearedNumbers(self, nums):

        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res


nums1 = [1, 3, 3]
print(Solution.findDisappearedNumbers(Solution, nums1))

# i feel like there's a way to do this with summation
# my test case was what was breaking it earlier, silly me