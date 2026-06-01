from typing import List

"""
Approach 1: Let's say the cost array has size n. Let's define an array A where
A[i] is the miminum cost to go from step i to the top of the stairs (ending
after covering step n-1). For our base cases, we have:

        A[n-1] = cost[n-1] -> since this is the only way from step n-1
        A[n-2] = cost[n-2] -> since going through n-1 cannot help minimizing
        
For any other case, since we can choose to take either 1 or 2 steps, we may use
the following recursion:

        A[i] = cost[i] + min(A[i+1], A[i+2])
        
We can fill array A iteratively from A[n-1] to A[0]. When we're done, the answer
will be min(A[0], A[1])
        
Example 1: cost = [1, 2, 3] 
           A    = [3, 2, 3] 
                -> ans = 2

Example 2: cost = [1, 2, 1, 2, 1, 1, 1] 
           A    = [4, 5, 3, 3, 2, 1, 1] 
                -> ans = 4
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Returning values for base cases
        if len(cost) == 1: return cost[0]
        if len(cost) == 2: return min(cost[1], cost[0]) 
        
        # Array of minimal costs:
        A = len(cost)*[0]
        A[len(cost)-1] = cost[len(cost)-1]
        A[len(cost)-2] = cost[len(cost)-2]
        
        for i in range(len(cost)-3,-1,-1):
            A[i] = cost[i] + min(A[i+1], A[i+2]) 

        return min(A[0], A[1])
    

sol1 = Solution()
print(sol1.minCostClimbingStairs([1,2]))
print(sol1.minCostClimbingStairs([2,1]))
print(sol1.minCostClimbingStairs([1,2,3]))
print(sol1.minCostClimbingStairs([1,2,1,2,1,1,1]))