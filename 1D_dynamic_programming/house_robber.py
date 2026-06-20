from typing import List
 
"""
Approach 1: Let's define array A to such that:

    A[i] := maximun money we can rob considering the nums vector from 0 to i.
    
We'll certainly have A[0] = nums[0]. 
when we add a house at i=1, we'll have A[1] = max{nums[0], nums[1]}.
For A[2], we must choose wether we should include house 2 or keep the best solution we had untill
the A[1]. 
It gets clear that, for any house i we add to the calculation of A[i], we can consider only two scenarios:
    1. We include the value nums[i] and sum it to the best case we had for A[i-2]
    2. We don't include value nums[i] and keep the value for A[i-1]
More formaly, we have:
    A[i] := max( (nums[i] + A[i-2]) , A[i-1] )
We'll do this iteratively from the bottom up, because it is more efficient than recursively.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Base cases
        A = len(nums)*[-1]
        A[0] = nums[0]
        
        if len(nums) == 1:
            return A[0]
        
        A[1] = max(nums[0],nums[1])
                    
        for i in range(2,len(nums)):
            A[i] = max((nums[i] + A[i-2]) , A[i-1])
        
        return A[len(nums)-1]
    
sol1 = Solution()
nums = [2,9,8,3,6]
print(sol1.rob(nums))
nums = [1,1,3,3]
print(sol1.rob(nums))
nums = [1,3]
print(sol1.rob(nums))
    
