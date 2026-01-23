#Greedy Algorithm

def intToRoman(num: int) -> str:
    # Define mappings in descending order
    val_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    # output=[]
    # for value, symbol in val_map:
    #     while num >= value:
    #         num -= value
    #         output.append(symbol)
    #
    # return "".join(output)



    roman_num = ""

    for value, symbol in val_map:
        # Determine how many times the symbol fits into the number
        count = num // value
        roman_num += symbol * count
        # Update the number to the remaining value
        num %= value

    return roman_num

if __name__ == '__main__':
    print(intToRoman(3549))  # Output: MMMDXLIX