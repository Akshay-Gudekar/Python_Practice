def get_pascals_row(row_index: int):
    """
    Returns the n-th row of Pascal's Triangle.
    Uses the formula: C(n, i) = C(n, i-1) * (n - i + 1) / i
    """
    row = [1]  # The first element is always 1

    current_val = 1
    for i in range(1, row_index + 1):
        # We use floor division // to keep results as integers
        # Formula: previous_val * (n - i + 1) / i
        current_val = current_val * (row_index - i + 1) // i
        row.append(current_val)

    return row


if __name__ == "__main__":
    # Test the function
    try:
        user_input = int(input("Enter the row index (starting from 0): "))
        if user_input < 0:
            print("Please enter a non-negative integer.")
        else:
            result = get_pascals_row(user_input)
            print(f"Row {user_input}: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")