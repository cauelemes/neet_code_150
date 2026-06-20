from typing import List

"""
Approach 1: Start with one pointer for each extreme of the list. Sum the values they point to and 

    if the sum is greater than the target: decrease the right pointer
    if the sum is less than the target: increase left pointer
    if the sum is equal to the target: return the pointers positions

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers)-1
        
        while l < r:
            
            sum = numbers[l] + numbers[r]
            # print("[", l, ",", r, "], sum=", sum) (*)
            
            if sum > target:
                r-=1
            elif sum < target:
                l+=1
            else:
                break
        
        return [l+1,r+1]
    
sol1 = Solution()

numbers = [1,2,3,4]
target = 3
print(sol1.twoSum(numbers, target))


