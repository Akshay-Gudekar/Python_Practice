"""
PYTHON INTERVIEW REVISION KIT (Parts 7, 8, & 9)
Total: 15 Coding Questions
"""

import math
from collections import Counter

# ==========================================
# PART 7: BASICS & STRING MANIPULATION
# ==========================================

# 1. Find the Second Largest Number
def second_largest(lst):
    """
    LOGIC: Use set() to remove duplicates (e.g., [10, 10, 2] becomes {10, 2}).
    Then sort and pick the second to last index.
    COMPLEXITY: T: O(N log N) due to sorting | S: O(N) to store the set.
    """
    unique_elements = list(set(lst))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort()
    return unique_elements[-2]

# 2. Check if String Has All Unique Characters
def has_unique_chars(s):
    """
    LOGIC: Compare length of string vs length of set(string).
    set() removes duplicates; if length changes, it wasn't unique.
    COMPLEXITY: T: O(N) | S: O(N) for the set storage.
    """
    return len(s) == len(set(s))

# 3. Find GCD of Two Numbers
def gcd(a, b):
    """
    LOGIC: Uses math.gcd(), which implements the Euclidean Algorithm.
    It repeatedly replaces 'a' with 'b' and 'b' with 'a % b' until b is 0.
    COMPLEXITY: T: O(log(min(a, b))) | S: O(1).
    """
    return math.gcd(a, b)

# 4. Count Uppercase and Lowercase Letters
def count_case(s):
    """
    LOGIC: Generator expression inside sum(). isupper() and islower()
    are built-in string methods to categorize characters.
    COMPLEXITY: T: O(N) | S: O(1).
    """
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# 5. Find Longest Word in a Sentence
def longest_word(s):
    """
    LOGIC: split() creates a list of words. max() with key=len finds
    the word with the highest character count.
    COMPLEXITY: T: O(N) where N is chars in sentence | S: O(W) where W is words.
    """
    words = s.split()
    return max(words, key=len) if words else ""


# ==========================================
# PART 8: BITWISE, STRINGS & STACKS
# ==========================================

# 6. Check if Number Is Power of Two
def is_power_of_two(n):
    """
    LOGIC: Bitwise AND. Powers of 2 have only one '1' in binary (e.g., 8 = 1000).
    8 & 7 (1000 & 0111) equals 0.
    COMPLEXITY: T: O(1) | S: O(1).
    """
    return n > 0 and (n & (n - 1)) == 0

# 7. Remove All Whitespaces from String
def remove_spaces(s):
    """
    LOGIC: split() without arguments splits by any whitespace (tabs, spaces, newlines).
    "".join() concatenates them back together.
    COMPLEXITY: T: O(N) | S: O(N).
    """
    return "".join(s.split())

# 8. Find First Non-Repeating Character
def first_unique(s):
    """
    LOGIC: Counter(s) creates a frequency map {char: count}.
    We then loop through the string to find the first char with count 1.
    COMPLEXITY: T: O(N) | S: O(1) (Alphabet size is fixed at 26-256).
    """
    freq = Counter(s)
    for c in s:
        if freq[c] == 1:
            return c
    return None

# 9. Rotate List by k Positions
def rotate_list(lst, k):
    """
    LOGIC: Slice the list. k % len(lst) handles rotations larger than the list size.
    lst[-k:] gets the end part, lst[:-k] gets the front.
    COMPLEXITY: T: O(N) | S: O(N) (due to list slicing creating copies).
    """
    if not lst: return lst
    k %= len(lst)
    return lst[-k:] + lst[:-k]

# 10. Check Balanced Parentheses
def is_balanced(s):
    """
    LOGIC: Uses a Stack (List). Push opening brackets. For closing brackets,
    pop from stack and check if it matches the pair.
    COMPLEXITY: T: O(N) | S: O(N).
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack


# ==========================================
# PART 9: OPTIMIZATION & ALGORITHMS
# ==========================================

# 11. Find Pair With Given Sum (Two-Sum)
def has_pair(nums, target):
    """
    LOGIC: Use a Hash Set (seen). For every number, check if (target - n)
    exists in the set. This avoids a nested O(N^2) loop.
    COMPLEXITY: T: O(N) | S: O(N).
    """
    seen = set()
    for n in nums:
        if target - n in seen:
            return True
        seen.add(n)
    return False

# 12. Remove All Occurrences of an Element
def remove_all(lst, x):
    """
    LOGIC: List comprehension creates a new list excluding 'x'.
    COMPLEXITY: T: O(N) | S: O(N).
    """
    return [i for i in lst if i != x]

# 13. Find Length Without len()
def str_length(s):
    """
    LOGIC: Manual iteration using a counter. Demonstrates basic loop logic.
    COMPLEXITY: T: O(N) | S: O(1).
    """
    count = 0
    for _ in s:
        count += 1
    return count

# 14. Convert List to Dictionary
def list_to_dict(keys, values):
    """
    LOGIC: zip() pairs elements from two lists. dict() converts pairs into key-values.
    COMPLEXITY: T: O(N) | S: O(N).
    """
    return dict(zip(keys, values))

# 15. Find Common Prefix
def common_prefix(strs):
    """
    LOGIC: Assume the first word is the prefix. Shorten it one character
    at a time until it matches the start of the next word.
    COMPLEXITY: T: O(Sum of all characters) | S: O(1).
    """
    if not strs: return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix: return ""
    return prefix

# ==========================================
# RUNNING THE TESTS (MANUAL CHECK)
# ==========================================
if __name__ == "__main__":
    print(f"1. Second Largest: {second_largest([10, 20, 4, 45, 99])}")
    print(f"2. Unique Chars: {has_unique_chars('python')}")
    print(f"3. GCD of 20, 28: {gcd(20, 28)}")
    print(f"4. Case Count: {count_case('PyThOn')}")
    print(f"5. Longest Word: {longest_word('Python coding interviews are easy')}")
    print(f"6. Power of Two: {is_power_of_two(16)}")
    print(f"7. Remove Spaces: {remove_spaces('Py th on')}")
    print(f"8. First Unique: {first_unique('swiss')}")
    print(f"9. Rotate List: {rotate_list([1, 2, 3, 4, 5], 2)}")
    print(f"10. Balanced: {is_balanced('({[]})')}")
    print(f"11. Pair Exists: {has_pair([2, 7, 11, 15], 9)}")
    print(f"12. Remove All 2s: {remove_all([1, 2, 3, 2, 4], 2)}")
    print(f"13. String Length: {str_length('python')}")
    print(f"14. List to Dict: {list_to_dict(['a', 'b'], [1, 2])}")
    print(f"15. Common Prefix: {common_prefix(['flower', 'flow', 'flight'])}")