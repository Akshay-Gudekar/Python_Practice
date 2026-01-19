class Solution:
    def multiply(self, a: int, b: int) -> int:
        # 1. Determine the sign
        negative = (a < 0) != (b < 0)
        a, b = abs(a), abs(b)

        res = 0

        # 2. Bitwise Multiplication Logic
        while b > 0:
            # If the multiplier (b) is odd, add the current 'a' to result
            # (b & 1) checks if the last bit is 1 (i.e., it's odd)
            if b & 1:
                res += a

            # Double 'a' and halve 'b'
            a <<= 1  # a = a * 2
            b >>= 1  # b = b // 2

        return -res if negative else res


# --- Testing ---
if __name__ == "__main__":
    sol = Solution()
    print(f"5 * 3 = {sol.multiply(5, 3)}")  # Output: 15
    print(f"-6 * 7 = {sol.multiply(-6, 7)}")  # Output: -42