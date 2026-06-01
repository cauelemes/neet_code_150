""""
Approach 1: let's consider an array A where A[i] is the number of disticnt ways
to climb a stair with i steps considering you can do it with either 1 or 2 steps
at a time. The base cases are:
    A[0] = 1 (makes it work)
    A[1] = 1
Pattern: it's basically the same problem of counting how many ways you can sum
3 coins using coins of value 1 and value 2. From a position A[i] we can have
arrived to it from lower position by either summing 1 or summing 2. So we can
use the following recursion:

    A[i] = A[i-2] + A[i-1]
    
We can build this array using an array and building it from the base through
an iteration.
Space complexity O(n)* -> Array size
Time complexity: O(n)* -> Array linear traversal
We could consider both just O(1), since n is no bigger than 45.

"""

class Solution:
    def climbStairs(self, n: int) -> int:

        # Base cases
        if n == 0 or n == 1: return 1
        
        # Initial array:
        A = (n+1)*[0]
        A[0] = 1
        A[1] = 1
        
        # Filling solutions iteratively
        for i in range(2,n+1):
            A[i] = A[i-1] + A[i-2]
        
        return A[n]
    

sol1 = Solution()
