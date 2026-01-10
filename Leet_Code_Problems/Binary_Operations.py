def add_binary(a, b):
    # return str(bin(int(a, 2) + int(b, 2))[2:]) ....... # my logic


    result = []
    carry = 0

    # Make strings equal length by padding with zeros
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        # Get bit value or 0 if index is out of bounds
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        # Calculate sum and carry
        total = bit_a + bit_b + carry
        result.append(str(total % 2))  # The bit to keep
        carry = total // 2  # The bit to carry

        i -= 1
        j -= 1

    return "".join(reversed(result))


print(add_binary("1010", "1100"))  # Output: 10110



# # Define two example numbers
# # a = 10 (Binary: 1010)
# # b = 6  (Binary: 0110)
# a = 10
# b = 6
#
# print(f"a: {a} (binary: {bin(a)[2:].zfill(4)})")
# print(f"b: {b} (binary: {bin(b)[2:].zfill(4)})")
# print("-" * 20)
#
# # 1. AND (&): Sets bit to 1 if both bits are 1
# print(f"AND (a & b): {a & b} (binary: {bin(a & b)[2:].zfill(4)})")
#
# # 2. OR (|): Sets bit to 1 if one of two bits is 1
# print(f"OR  (a | b): {a | b} (binary: {bin(a | b)[2:].zfill(4)})")
#
# # 3. XOR (^): Sets bit to 1 if only one of two bits is 1
# print(f"XOR (a ^ b): {a ^ b} (binary: {bin(a ^ b)[2:].zfill(4)})")
#
# # 4. NOT (~): Inverts all bits (Calculated as -(x + 1))
# print(f"NOT (~a):    {~a} (binary: {bin(~a)})")
#
# # 5. Left Shift (<<): Push bits left, fill right with zeros (multiplies by 2)
# print(f"Left Shift  (a << 1): {a << 1} (binary: {bin(a << 1)[2:]})")
#
# # 6. Right Shift (>>): Push bits right, discard far right (divides by 2)
# print(f"Right Shift (a >> 1): {a >> 1} (binary: {bin(a >> 1)[2:].zfill(4)})")