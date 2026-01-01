"""
PYTHON INTERVIEW PREPARATION KIT (Parts 8-11)
Total: 20 Essential Coding Challenges
"""

from collections import Counter


# =================================================================
# 1. MATHEMATICAL LOGIC & BITWISE
# =================================================================

def is_power_of_two(n):
    """
    Logic: A power of 2 (like 8: 1000) and n-1 (7: 0111) share no '1' bits.
    Using & (AND) will result in 0.
    Time Complexity: O(1)
    """
    return n > 0 and (n & (n - 1)) == 0


def count_digits(n):
    """
    Logic: Floor division (// 10) removes the last digit. We count how many times we can do this.
    Time Complexity: O(log10 N)
    """
    n = abs(n)
    if n == 0: return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def primes_upto(n):
    """
    Logic: Sieve-like approach. Check divisibility up to sqrt(n) for efficiency.
    Time Complexity: O(N * sqrt(N))
    """
    primes = []
    for num in range(2, n + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0: break
        else:
            primes.append(num)
    return primes


def is_pal_num(n):
    """
    Logic: Convert to string and use slicing to compare with reverse.
    Time Complexity: O(N)
    """
    return str(n) == str(n)[::-1]


# =================================================================
# 2. STRING MANIPULATION
# =================================================================

def remove_spaces(s):
    """
    Logic: .split() picks up all whitespace; .join() stitches it back with nothing.
    Time Complexity: O(N)
    """
    return "".join(s.split())


def first_unique(s):
    """
    Logic: Use a frequency map (Counter). Return the first char where count is 1.
    Time Complexity: O(N)
    """
    freq = Counter(s)
    for c in s:
        if freq[c] == 1: return c
    return None


def common_prefix(strs):
    """
    Logic: Shrink the prefix string until the start of every other string matches it.
    Time Complexity: O(Characters in list)
    """
    if not strs: return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix


def is_substring(s, sub):
    """ Logic: Python's 'in' operator is optimized for pattern matching. """
    return sub in s


def str_length(s):
    """ Logic: Manual iteration to demonstrate loop counting. """
    count = 0
    for _ in s: count += 1
    return count


# =================================================================
# 3. LISTS & ARRAY PROCESSING
# =================================================================

def rotate_list(lst, k):
    """
    Logic: Slicing the last k elements and moving them to the front.
    Time Complexity: O(N)
    """
    if not lst: return lst
    k %= len(lst)
    return lst[-k:] + lst[:-k]


def move_zeros(lst):
    """
    Logic: Filter non-zeros first, then append the count of zeros found.
    Time Complexity: O(N)
    """
    return [x for x in lst if x != 0] + [0] * lst.count(0)


def reverse_list_inplace(lst):
    """ Logic: Modifies the original list object in memory. Space: O(1) """
    lst.reverse()
    return lst


def remove_all(lst, x):
    """ Logic: List comprehension to build a new list without target x. """
    return [i for i in lst if i != x]


def min_max(lst):
    """ Logic: Single pass for each built-in. Time: O(N) """
    return min(lst), max(lst)


def list_to_string(lst):
    """ Logic: map converts integers to strings so join() works. """
    return "".join(map(str, lst))


# =================================================================
# 4. DATA STRUCTURES (SETS, DICTS, STACKS)
# =================================================================

def is_balanced(s):
    """
    Logic: Stack stores open brackets. Closers must match the top of the stack.

    Time Complexity: O(N)
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]: return False
    return not stack


def has_pair(nums, target):
    """
    Logic: Use a Set for O(1) lookups. Check if (target - current) was already seen.

    Time Complexity: O(N)
    """
    seen = set()
    for n in nums:
        if target - n in seen: return True
        seen.add(n)
    return False


def first_duplicate(lst):
    """ Logic: Use a set to track elements; the first time an element is 'seen' twice, return it. """
    seen = set()
    for x in lst:
        if x in seen: return x
        seen.add(x)
    return None


def list_to_dict(keys, values):
    """ Logic: zip() creates tuples (key, val), dict() converts them. """
    return dict(zip(keys, values))


def sort_by_value(d):
    """ Logic: Use sorted() with a lambda to target the value (index 1 of items). """
    return dict(sorted(d.items(), key=lambda x: x[1]))


# =================================================================
# EXECUTION & OUTPUT
# =================================================================

if __name__ == "__main__":
    print("--- PART 8-11 INTERVIEW RESULTS ---")
    print(f"1.  Is 16 Power of Two?      : {is_power_of_two(16)}")
    print(f"2.  Count Digits (12345)     : {count_digits(12345)}")
    print(f"3.  Primes up to 10          : {primes_upto(10)}")
    print(f"4.  Is 121 Palindrome?       : {is_pal_num(121)}")
    print(f"5.  Remove Whitespace        : '{remove_spaces('P y t h o n')}'")
    print(f"6.  First Unique in 'swiss'  : {first_unique('swiss')}")
    print(f"7.  Common Prefix            : {common_prefix(['flower', 'flow', 'flight'])}")
    print(f"8.  Is 'view' in 'interview' : {is_substring('interview', 'view')}")
    print(f"9.  Manual Length ('Python') : {str_length('Python')}")
    print(f"10. Rotate [1,2,3,4,5] by 2  : {rotate_list([1, 2, 3, 4, 5], 2)}")
    print(f"11. Move Zeros to End        : {move_zeros([0, 1, 0, 3, 12])}")
    print(f"12. Reverse In-place         : {reverse_list_inplace([1, 2, 3])}")
    print(f"13. Remove all 2s from [1,2,2,3]: {remove_all([1, 2, 2, 3], 2)}")
    print(f"14. Min/Max of [4,1,9,2]     : {min_max([4, 1, 9, 2])}")
    print(f"15. List to String [1,2,3]   : {list_to_string([1, 2, 3])}")
    print(f"16. Balanced '({[]})'        : {is_balanced('({[]})')}")
    print(f"17. Pair Sum (target 9)      : {has_pair([2, 7, 11, 15], 9)}")
    print(f"18. First Duplicate [3,1,3,4]: {first_duplicate([3, 1, 3, 4])}")
    print(f"19. List to Dict             : {list_to_dict(['a', 'b'], [1, 2])}")
    print(f"20. Sort Dict by Value       : {sort_by_value({'a': 3, 'b': 1})}")
    print("-" * 35)

"""
### EXPLAINING IN-BUILT FUNCTIONS USED:

1. zip(list1, list2):
   - Pairs elements from two iterables into tuples. Example: ['a', 'b'] + [1, 2] -> [('a', 1), ('b', 2)].

2. map(function, iterable):
   - Applies a function to every item in the list. We use map(str, lst) to convert every number 
     into a string before joining them.

3. set():
   - A collection that allows for O(1) average time complexity for lookups. Vital for finding 
     duplicates or pairs quickly.

4. sorted(iterable, key=...):
   - Returns a new sorted list. The 'key' argument (often a lambda) allows us to tell Python 
     exactly what to sort by (like dictionary values instead of keys).

5. collections.Counter:
   - A subclass of dictionary specifically designed to count hashable objects. 
     Extremely fast for frequency problems.

6. .join():
   - Concatenates a list of strings into one string, separated by the string you call it on.

7. .startswith():
   - Checks if a string begins with a specific prefix. Much cleaner than manual slicing.
"""