class Solution:
    def singleNumber(self, nums: List[int]) -> int:
     nums.sort()
     for j in range(0,len(nums)-1,2):  
        if nums[j]!=nums[j+1]:
            return nums[j]
       
     return(nums[-1]) 