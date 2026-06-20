from typing import List

"""
Approach 1 (naive): let's simply create a list, which we'll sort when we construct it and every time we
add a new number to it. Then we should simply pick the number at the position len(num)-k for every addition.

"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # we'll begin the constructor with numbers sorted, but maybe later we could set it
        # to use the add function
        self.nums = nums
        self.nums.sort() 
        self.k = k
        if (k>len(self.nums)):
            self.kth = -1
        else:
            self.kth = self.nums[len(self.nums)-self.k]

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        self.kth = self.nums[len(self.nums)-self.k]
        return self.kth
    
    
# nums = [1,2,3,3]
# target = 3
# obj1 = KthLargest(target, nums)
# print(obj1.nums)
# print(obj1.add(3))
# print(obj1.add(5))
# print(obj1.add(6))
# print(obj1.add(7))
# print(obj1.add(8))
# print(obj1.add(2))
# print(obj1.nums)




"""
Approach 2: Let's use python lists and sublist slicing methods underneath the hood. It's certainly not
the most optimized way of doing it, but it's okay as a first solution. 

We just need to keep the k greatest elements, because if a number smaller than the kth largest number is added,
it doesn't change which is the k-th largest number. On the other hand, if a number greater that the kth number
is added, it will push every lesser number one position to the left.

"""