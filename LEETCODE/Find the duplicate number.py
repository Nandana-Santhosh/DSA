'''Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right =  len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < (mid + 1):
                right = mid
            else:
                left = mid + 1
        return nums[left]