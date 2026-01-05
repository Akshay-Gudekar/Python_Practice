class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)
        
        for i in range(n):
            # Check if current value is smaller than the next value
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
                
        return total
    
# Example usage:
solution = Solution()
print(solution.romanToInt("MCMXCIV"))  # Output: 1994


import roman
i = roman.fromRoman("MCMIV")
j = roman.fromRoman("LV")
k = roman.fromRoman("XXIV")
print(i,j,k)