from collections import Counter
import string


# ==========================================
# CATEGORY 1: STRING MANIPULATION
# ==========================================

def reverse_string(s):
    # HOW IT WORKS: [::-1] is a slice that starts at the end and moves backwards by 1.
    return s[::-1]


def reverse_words(s):
    # HOW IT WORKS: s.split() breaks string into list; word[::-1] reverses each word;
    # " ".join() glues them back with spaces.
    return " ".join(word[::-1] for word in s.split())


def is_palindrome(s):
    # HOW IT WORKS: Normalizes text (lowercase/no spaces) and checks if it equals its reverse.
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]


def are_anagrams(s1, s2):
    # HOW IT WORKS: If both strings have same letters, their sorted lists will be identical.
    return sorted(s1.lower()) == sorted(s2.lower())


def count_vowels(s):
    # HOW IT WORKS: Loops through string and adds '1' to a sum for every char found in "aeiou".
    return sum(1 for char in s.lower() if char in "aeiou")


def char_frequency(s):
    # HOW IT WORKS: Counter() creates a dictionary mapping characters to their counts.
    return Counter(s)


def count_words(s):
    # HOW IT WORKS: split() defaults to whitespace; len() counts the resulting items.
    return len(s.split())


def to_title_case(s):
    # HOW IT WORKS: Built-in string method that capitalizes the first letter of every word.
    return s.title()


def remove_punctuation(s):
    # HOW IT WORKS: Joins only the characters that are NOT in the string.punctuation set.
    return ''.join(c for c in s if c not in string.punctuation)


# ==========================================
# CATEGORY 2: MATHEMATICAL LOGIC
# ==========================================

def find_missing(nums, n):
    # HOW IT WORKS: Uses the math formula (n*(n+1)/2) to find the sum it should have
    # been, then subtracts the actual sum to find the missing gap.
    return n * (n + 1) // 2 - sum(nums)


def is_armstrong(n):
    # HOW IT WORKS: Checks if n equals the sum of its digits raised to the power of digit count.
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)


def sum_of_digits(n):
    # HOW IT WORKS: Converts number to absolute string, iterates digits, and sums them.
    return sum(int(digit) for digit in str(abs(n)))


def factorial(n):
    # HOW IT WORKS: Recursively calls itself (n * n-1) until it hits the base case (1).
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    # HOW IT WORKS: Sums the result of the two previous Fibonacci calls.
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ==========================================
# CATEGORY 3: LISTS & COLLECTIONS
# ==========================================

def find_duplicates(lst):
    # HOW IT WORKS: Counts items and returns only those where the frequency is > 1.
    count = Counter(lst)
    return [item for item, freq in count.items() if freq > 1]


def is_sorted(lst):
    # HOW IT WORKS: Checks if the list is identical to a version sorted by Python.
    return lst == sorted(lst)


def common_elements(lst1, lst2):
    # HOW IT WORKS: Uses set intersection (&) to find unique items present in both.
    return list(set(lst1) & set(lst2))


def find_max(lst):
    # HOW IT WORKS: Returns the highest value in the iterable.
    return max(lst)


def flatten(lst):
    # HOW IT WORKS: Nested list comprehension: "for each list in big list, for each item in that list".
    return [item for sublist in lst for item in sublist]


# ==========================================
# ALL OUTPUTS (PRINTS EVERYTHING)
# ==========================================
if __name__ == "__main__":
    print(f"1.  Reverse String: {reverse_string('hello')}")
    print(f"2.  Reverse Words: {reverse_words('Python is fun')}")
    print(f"3.  Is Palindrome: {is_palindrome('Race car')}")
    print(f"4.  Are Anagrams: {are_anagrams('listen', 'silent')}")
    print(f"5.  Count Vowels: {count_vowels('Python is fun')}")
    print(f"6.  Char Frequency: {dict(char_frequency('python'))}")
    print(f"7.  Count Words: {count_words('Python is awesome')}")
    print(f"8.  Title Case: {to_title_case('python is fun')}")
    print(f"9.  Remove Punctuation: {remove_punctuation('Hello, World!')}")
    print(f"10. Find Missing (1-5): {find_missing([1, 2, 4, 5], 5)}")
    print(f"11. Is 153 Armstrong: {is_armstrong(153)}")
    print(f"12. Sum of Digits: {sum_of_digits(1234)}")
    print(f"13. Factorial of 5: {factorial(5)}")
    print(f"14. Fibonacci(6): {fibonacci(6)}")
    print(f"15. Duplicates in [1,2,3,2,1]: {find_duplicates([1, 2, 3, 2, 4, 1])}")
    print(f"16. Is List Sorted: {is_sorted([1, 2, 3, 4])}")
    print(f"17. Common Elements: {common_elements([1, 2, 3], [2, 3, 4])}")
    print(f"18. Find Max: {find_max([3, 7, 2, 9, 5])}")
    print(f"19. Flatten List: {flatten([[1, 2], [3, 4], [5]])}")

    # Simple Swap Output
    a, b = 5, 10
    a, b = b, a
    print(f"20. Swap Variables: a={a}, b={b}")