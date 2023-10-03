''' You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true '''
class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        for i in range(len(nums)):
            if nums[i]==0:
                if(i==0 or nums[i-1]==0) and (i==len(nums)-1 or nums[i+1]==0):
                    n-=1
                    nums[i]=1
            if n<=0:
                return True
        return False