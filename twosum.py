class Solution:
  def twoSum(self, nums, target):
    hash_table = {} # {number : index}
    for i in range(len(nums)):
      difference = target - nums[i]
      if difference in hash_table:
        return [hash_table[difference], i]
      hash_table[nums[i]] = i
      # print(hash_table) # print each iteration for debugging

# tests

# nums1 = [2, 7, 11, 15]
# nums2 = [3, 5, 12, 9, 8, 5]
# nums3 = [24, 9523, 32, 25, 263, 236, 923]
# print(Solution.twoSum(Solution, nums1, 9))
# print(Solution.twoSum(Solution, nums2, 21))
# print(Solution.twoSum(Solution, nums3, 1159))

# here's a faster solution from the solutions tab;
# it looks like there's just a small switch up right before the return statement
# let's come back to that at a later date for review.
# for now remember that you can employ a hash map
# and it's almost always going to be quicker than a nested for loop.

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numToIndex = {}
#         for i in range(len(nums)):
#             if target - nums[i] in numToIndex:
#                 return [numToIndex[target - nums[i]], i]
#             numToIndex[nums[i]] = i
#         return []