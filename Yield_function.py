# def generate_numbers():
#     for i in range(5):
#         yield i
#
# gen = generate_numbers()
#
# print(next(gen))  # Output: 0
# print(next(gen))  # Output: 1
# print(list(gen))  # Output: [2, 3, 4]

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        c = a + b
        a = b
        b = c

for num in fibonacci(10):
    print(num, end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34