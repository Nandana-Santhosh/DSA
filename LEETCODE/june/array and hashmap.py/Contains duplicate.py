'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true '''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new=set(nums)
        if len(new) == len(nums):
            return False
        if new==nums:
            return False
        return True
    

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        new=nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
    

    class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                 return True
        return False //complexity o(n^2)

        
        
        
        