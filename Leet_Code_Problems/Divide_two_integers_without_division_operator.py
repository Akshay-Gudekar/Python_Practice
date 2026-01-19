import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # My Approach
        # division = dividend / divisor
        # return int(division)

        # All things need to care about

        # 1. Handle the 32-bit integer overflow edge case
        # Range: [-2^31, 2^31 - 1] -> [-2147483648, 2147483647]
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # 2. Determine the sign of the result
        # If one is negative and the other is positive, the result is negative
        negative = (dividend < 0) != (divisor < 0)

        # 3. Work with absolute values to simplify logic
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        # 4. Use bit shifting to find how many times 'b' fits into 'a'
        while a >= b:
            temp_divisor = b
            multiple = 1

            # Double the divisor as much as possible using left shift (<< 1)
            # This is like checking: Is a >= b*2? Is a >= b*4? Is a >= b*8?
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            # Subtract the largest found multiple from 'a'
            a -= temp_divisor
            quotient += multiple

        # 5. Apply the sign and return
        return -quotient if negative else quotient


# --- Testing the code ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Result of 10 / 3: {sol.divide(10, 3)}")  # Expected: 3
    print(f"Result of 7 / -3: {sol.divide(7, -3)}")  # Expected: -2
    print(f"Result of overflow: {sol.divide(-2147483648, -1)}")  # Expected: 2147483647