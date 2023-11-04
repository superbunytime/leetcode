# import time
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) != len(set(nums)):
#             return True
#         return False
    
# # tests

nums1 = [1, 1, 1, 3]
nums2 = [1, 2, 3, 4, 5]

# start = time.time()
# print(Solution.containsDuplicate(Solution, nums1))
# end = time.time()
# print(end - start)

# start = time.time()
# print(Solution.containsDuplicate(Solution, nums2))
# end = time.time()
# print(end - start)

# okay for python specifically that's really easy with set.
# but is it more efficient using a hash map?
# let's code that up and run a cron job on each one.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_table = {} # {number : index}
        for i in range(len(nums)):
            print(i)
            if i in hash_table:
                return True
            hash_table[i] = nums[i]
        print(hash_table)
        
print(Solution.containsDuplicate(Solution, nums1))
print(Solution.containsDuplicate(Solution, nums2))

# unfortunately, i don't have all day to spend on this.
# the set solution works, even though it's pretty inefficient.
# gonna copy-paste the optimal solution and try to parse it.
# before looking, i'm certain it will involve a properly coded hashmap.
# nvm they all use sets maybe mine wasn't that bad.
