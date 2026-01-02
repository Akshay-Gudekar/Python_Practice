
s = "a4b2c3"
it = iter(s)

# zip(it, it) takes two elements at a time from the same iterator
for char, count in zip(it, it):
    print(char * int(count))



#
# s = "abc"
# it = iter(s)
#
# print(next(it)) # Output: 'a'
# print(next(it)) # Output: 'b'
# print(next(it)) # Output: 'c'
# # print(next(it)) # This would raise a StopIteration error