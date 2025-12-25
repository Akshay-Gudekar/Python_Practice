"""
PYTHON INTERVIEW PREPARATION & REVISION FILE
--------------------------------------------
Concepts covered: String Slicing, List Comprehensions, Recursion, 
Mathematical Series, Set Logic, and the Collections module.
"""

from collections import Counter
import string


# ==============================================================================
# CATEGORY 1: STRING MANIPULATION
# ==============================================================================

def reverse_string(s):
    """
    LOGIC: Python String Slicing [start:stop:step].
    OPERATION: Using [::-1] takes the whole string and steps backward by 1.
    COMPLEXITY: O(n) - visits each character once.
    """
    # HOW IT WORKS: [::-1] is a slice that starts at the end and moves backwards by 1.
    return s[::-1]  # Output Example: "olleh"


def reverse_words(s):
    """
    LOGIC: Split -> Transform -> Join.
    OPERATION: 
        1. s.split() creates a list of words.
        2. 'for word in' loop picks one word at a time.
        3. word[::-1] reverses that specific word.
        4. " ".join() merges them back into a single string.
    """
    # HOW IT WORKS: s.split() breaks string into list; word[::-1] reverses each word;
    # " ".join() glues them back with spaces.
    return " ".join(word[::-1] for word in s.split())  # Output Example: "nohtyP si nuf"


def is_palindrome(s):
    """
    LOGIC: Normalization and Equality check.
    OPERATION: Removes spaces and forces lowercase so "Race car" matches "racecar".
    """
    # HOW IT WORKS: Normalizes text (lowercase/no spaces) and checks if it equals its reverse.
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]  # Output Example: True


def are_anagrams(s1, s2):
    """
    LOGIC: Character Sorting Comparison.
    OPERATION: sorted() returns a list of characters in alphabetical order. 
               If two words are anagrams, their sorted lists are identical.
    """
    # HOW IT WORKS: If both strings have same letters, their sorted lists will be identical.
    return sorted(s1.lower()) == sorted(s2.lower())  # Output Example: True


def count_vowels(s):
    """
    LOGIC: Membership testing with Generator Expression.
    OPERATION: 
        1. The 'for char in s' loop visits every character.
        2. 'if char in "aeiou"' checks against a reference string.
        3. sum() adds a '1' for every character that passes the check.
    """
    # HOW IT WORKS: Loops through string and adds '1' to a sum for every char found in "aeiou".
    return sum(1 for char in s.lower() if char in "aeiou")  # Output Example: 4


def char_frequency(s):
    """
    LOGIC: Hash Map / Dictionary counting.
    OPERATION: Counter(s) iterates the string once and maps characters to counts.
    COMPLEXITY: O(n)
    """
    # HOW IT WORKS: Counter() creates a dictionary mapping characters to their counts.
    return Counter(s)  # Output Example: {'p': 1, 'y': 1, ...}


def count_words(s):
    """
    LOGIC: Tokenization based on whitespace.
    OPERATION: split() creates a list of elements separated by spaces; len() counts them.
    """
    # HOW IT WORKS: split() defaults to whitespace; len() counts the resulting items.
    return len(s.split())  # Output Example: 3


def to_title_case(s):
    """
    LOGIC: Built-in transformation.
    OPERATION: Internally loops through the string and uppercases letters following spaces.
    """
    # HOW IT WORKS: Built-in string method that capitalizes the first letter of every word.
    return s.title()  # Output Example: "Python Is Fun"


def remove_punctuation(s):
    """
    LOGIC: Filtering using a reference set.
    OPERATION: 
        1. 'for c in s' iterates every character.
        2. 'if c not in string.punctuation' filters out symbols.
        3. .join() combines the kept characters.
    """
    # HOW IT WORKS: Joins only the characters that are NOT in the string.punctuation set.
    return ''.join(c for c in s if c not in string.punctuation)  # Output Example: "Hello World"


# ==============================================================================
# CATEGORY 2: MATHEMATICAL LOGIC
# ==============================================================================

def find_missing(nums, n):
    """
    LOGIC: Arithmetic Series (Gauss Summation).
    OPERATION: 
        1. n*(n+1)//2 finds the sum the list *should* have.
        2. sum(nums) finds the actual current total.
        3. Subtracting them reveals the missing "gap".
    """
    # HOW IT WORKS: Uses the math formula (n*(n+1)/2) to find the sum it should have
    # been, then subtracts the actual sum to find the missing gap.
    return n * (n + 1) // 2 - sum(nums)  # Output Example: 3



def is_armstrong(n):
    """
    LOGIC: Digit power-summation.
    OPERATION: 
        1. str(n) allows iteration over digits.
        2. len(digits) determines the power to raise digits to.
        3. sum() totals each digit raised to that power.
    """
    # HOW IT WORKS: Checks if n equals the sum of its digits raised to the power of digit count.
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)  # Output Example: True


def sum_of_digits(n):
    """
    LOGIC: Absolute value string summation.
    OPERATION: 1. abs(n) handles negatives. 2. Loops each character, converts back to int, and sums.
    """
    # HOW IT WORKS: Converts number to absolute string, iterates digits, and sums them.
    return sum(int(digit) for digit in str(abs(n)))  # Output Example: 10


def factorial(n):
    """
    LOGIC: Recursion with Base Case.
    OPERATION: Calls itself with (n-1) until it hits 1. No loop; uses the call stack.
    COMPLEXITY: O(n)
    """
    # HOW IT WORKS: Recursively calls itself (n * n-1) until it hits the base case (1).
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # Output Example: 120


def fibonacci(n):
    """
    LOGIC: Recursive Tree.
    OPERATION: Calculates F(n) by summing F(n-1) and F(n-2).
    COMPLEXITY: O(2^n) - Note: Use memoization or loops for better performance.
    """
    # HOW IT WORKS: Sums the result of the two previous Fibonacci calls.
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Output Example: 8



# ==============================================================================
# CATEGORY 3: LISTS & COLLECTIONS
# ==============================================================================

def find_duplicates(lst):
    """
    LOGIC: Frequency filtering.
    OPERATION: 
        1. Counter(lst) counts occurrences.
        2. Loop checks the count (freq) of each item.
        3. Returns items where freq > 1.
    """
    # HOW IT WORKS: Counts items and returns only those where the frequency is > 1.
    count = Counter(lst)
    return [item for item, freq in count.items() if freq > 1]  # Output Example: [1, 2]


def is_sorted(lst):
    """
    LOGIC: Equality check against sorted state.
    OPERATION: sorted(lst) creates a new sorted list; == compares them index-by-index.
    """
    # HOW IT WORKS: Checks if the list is identical to a version sorted by Python.
    return lst == sorted(lst)  # Output Example: True


def common_elements(lst1, lst2):
    """
    LOGIC: Set Intersection (Hashing).
    OPERATION: Converts lists to sets (unique values) and finds the overlap using '&'.
    COMPLEXITY: O(n + m) - much faster than a nested for-loop.
    """
    # HOW IT WORKS: Uses set intersection (&) to find unique items present in both.
    return list(set(lst1) & set(lst2))  # Output Example: [2, 3]


def find_max(lst):
    """
    LOGIC: Single-pass iteration.
    OPERATION: max() keeps track of the largest value seen while looping through the list once.
    """
    # HOW IT WORKS: Returns the highest value in the iterable.
    return max(lst)  # Output Example: 9


def flatten(lst):
    """
    LOGIC: Nested List Comprehension.
    OPERATION: 
        1. Outer loop 'for sublist in lst' grabs each inner list.
        2. Inner loop 'for item in sublist' grabs each value.
        3. Logic is like: for sublist in lst: for item in sublist: append(item)
    """
    # HOW IT WORKS: Nested list comprehension: "for each list in big list, for each item in that list".
    return [item for sublist in lst for item in sublist]  # Output Example: [1, 2, 3, 4, 5]


# ==============================================================================
# ALL OUTPUTS (PRINTS EVERYTHING)
# ==============================================================================
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
    # HOW IT WORKS: Creates a temporary tuple (b, a) then unpacks it back to a and b.
    a, b = 5, 10
    a, b = b, a
    print(f"20. Swap Variables: a={a}, b={b}")
