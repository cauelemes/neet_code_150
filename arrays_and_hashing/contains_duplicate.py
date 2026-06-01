from typing import List


"""
Approach 1: for each number, search compare it to every other number. 
Time complexity: O(n²).
Space complexity: O(1).
"""
def hasDuplicate1(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] == nums[j]):
                return True
            
    return False


""" 
Approach 2: use set data structure. We go through the nums list and add one
element at a time to the set. For every adition, we check wether the
size of that set increase with the addition, and if it didn't, we
immediately return True. If that is never the case, we return False. 
A set is hash-based and only take O(1) average time for adding elements,
as well as for checking its lenghth
Time complexity: O(n)
Space complexity: O(n)
"""
def hasDuplicate2(nums: List[int]) -> bool:
    nums_set = set()
    set_size=len(nums_set)
    for i in range(len(nums)):
        nums_set.add(nums[i])
        
        # if the size has not changed
        new_size = len(nums_set)
        if new_size == set_size:
            return True
        
        # if it has changed, we update it
        set_size = new_size
        
    return False

# nums=[1,2,3,4]
# print(hasDuplicate2(nums))
# nums=[1,2,2,3,4]
# print(hasDuplicate2(nums))



