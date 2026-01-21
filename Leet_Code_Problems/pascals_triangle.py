from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the triangle with the first row
        triangle = [[1]]

        for i in range(1, numRows):
            # Start every row with a 1
            row = [1]
            # Get the previous row to calculate current row values
            prev_row = triangle[i - 1]

            # Fill in the middle values
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])

            # End every row with a 1
            row.append(1)
            triangle.append(row)

        return triangle


# --- TEST IN PYCHARM ---
if __name__ == "__main__":
    sol = Solution()
    n = 5
    result = sol.generate(n)

    # Print it formatted like a triangle
    for row in result:
        print(" ".join(map(str, row)).center(n * 3))