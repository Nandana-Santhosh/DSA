'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]*n
        post=[1]*n
        ans=[1]*n

        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            post[i]=post[i+1]*nums[i+1]

        ans=[pre[i]*post[i] for i in range(n)]
        return ans