from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1
        ans = -1
        
        count = 0
        while l <= r :
            
            # get the (sub)list middle term index (floored)
            m = (l+r)//2
            
            # need to search right half
            if target > nums[m]:
                l = m + 1
            # need to search left half
            if target < nums[m]:
                r = m - 1
            # we've found the number   
            if target == nums[m]:
                ans = m  
                break   
        # if not found
        return ans
        
        


sol1 = Solution()

nums = [-1,0,2,4,6,8]
target = 4
print(sol1.search(nums, target))

nums = [-1,0,2,4,6,8]
target = 3