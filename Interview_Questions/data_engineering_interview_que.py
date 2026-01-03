
s = "a4b2c3"
it = iter(s)

# zip(it, it) takes two elements at a time from the same iterator
for char, count in zip(it, it):
    print(char * int(count))

#slicing approach
for i in range(0, len(s), 2):
    char = s[i]
    count = int(s[i+1])
    print(char * count)

#
# s = "abc"
# it = iter(s)
#
# print(next(it)) # Output: 'a'
# print(next(it)) # Output: 'b'
# print(next(it)) # Output: 'c'
# # print(next(it)) # This would raise a StopIteration error

# s = "a10b2"
# char = ""
# num_str = ""
#
# for i, item in enumerate(s):
#     if item.isalpha():
#         char = item
#     else:
#         num_str += item
#         # If it's the last character or the next one is a letter, print
#         if i + 1 == len(s) or s[i+1].isalpha():
#             print(char * int(num_str))
#             num_str = "" # Reset for the next pair

# s = "a4b2c3"
# char = ""
#
# for item in s:
#     if item.isalpha():
#         # Store the character to use later
#         char = item
#     elif item.isdigit():
#         # Multiply the stored character by the current digit
#         print(char * int(item))
1

2

3

4

5

6

7

8

9

10

11

# Achieve the below output using given input
# given input a4b2c3 Expected output aaaabbccc
# str="a4b2c3"
# final_char=""
# for i in str:
#     if i.isdigit():
#         index=str.find(i)
#         char=str[index-1]
#         for j in range(0,int(i)):
#             final_char=final_char+char
# print("final_char : ",final_char)
