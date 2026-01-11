class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # Use two variables to track previous steps (Fibonacci approach)
        first, second = 1, 2

        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current

        return second
sol= Solution()
print(sol.climbStairs(5))
# Time Complexity: O(n) — we iterate through the steps once.
# Space Complexity: O(1) — we only store two integer variables regardless of n.
#
# Why this works:
# Base Cases: If there's 1 step, there is 1 way. If there are 2 steps, there are 2 ways (1+1 or 2).
# Iteration: We start from the 3rd step and continuously add the possibilities of the previous two steps,
# shifting our "pointers" forward as we go.