from typing import List

"""
Approach 2: start by ordering the list O(n*lg(n)). Create two pointers by the extremes of the list.
Check wether these extreme values sum the target. If the sum is greater than the target, we should
move the right pointer down to the left and try again. If the sum is less than the target, we should
move the left pointer up to the right. Do this untill we reach the target or run out of numbers, which
is takes O(n) time.
Time complexity:  O(n*lg(n))
Space complexity: O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # We must furst find a way to keep the original indexes before sorting, so we'll create a List of pairs
        # where the the first number is the value and the second is the original index.
        nums_idxs=[]
        for i, num in enumerate(nums):
            nums_idxs.append((num,i))
            
        # We sort in place, which will use the num value first
        nums_idxs.sort()

        l = 0
        r=len(nums)-1
        
        while (l<r):
            
            sum = nums_idxs[l][0] + nums_idxs[r][0]
            
            # if we sum the target, we're done
            if sum == target:
                
                # We should just make sure we return in the format (i,j), where i < j
                # This could be inverted if the comparissons use negative numbers
                i = min(nums_idxs[l][1], nums_idxs[r][1])
                j = max(nums_idxs[l][1], nums_idxs[r][1])
                return([i,j])

            if sum < target:
                l+=1
            else:
                r-=1
                
        # Since a solution is guaranteed, this should never happen
        return([])
    
    
sol = Solution()
nums = [3,4,5,6]
target = 7
print(sol.twoSum(nums, target))

nums = [4,5,6]
target = 10
print(sol.twoSum(nums, target))

nums = [5,5]
target = 10
print(sol.twoSum(nums, target))

nums=[3,2,3]
target=6
print(sol.twoSum(nums, target))


# A = []
# nums=[3,2,3]
# for i, num in enumerate(nums):
#     A.append((num, i))
             
             
# print(A)
# A.sort()
# print(A)



"""
Approach 1 (naive): for each number in nums, check wether the number it needs to be summed
with to reach the target is in the list.
Time complexity:  O(n²)
Space complexity: O(1)
"""

