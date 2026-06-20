from typing import List
import heapq
 
"""
Approach 3: We'll use a min heap of size k. The heap will basically have the kth biggest element at the
top. Elements bigger than the kth will be positioned at lower nodes. Elements smaller that the kth will
not be in the heap at all (considering cases where the amount of numbers given by the stream has already
reached k)

"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        heapq.heapify(self.nums)
        for x in nums:
            self.add(x)
            
            
    def add(self, val: int) -> int:
        # We need only store k biggest elements
        if len(self.nums) >= self.k:
            if val > self.nums[0]:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, val)
        else:
            heapq.heappush(self.nums, val)   
                
        return self.nums[0]
    
    
nums = [4, 5, 8, 2]
target = 3

# nums = []
# target = 1
# nums = [1000, -1000]
# target = 3
obj1 = KthLargest(target, nums)
print(obj1.nums)
print(obj1.add(0))
print(obj1.nums)
print(obj1.add(2))
print(obj1.nums)
print(obj1.add(-3))
print(obj1.nums)
print(obj1.add(1000))
print(obj1.nums)
print(obj1.add(9))
print(obj1.nums)
print(obj1.add(4))
print(obj1.nums)
