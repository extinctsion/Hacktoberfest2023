"""
Problem : String to Integer (atoi)

📌 Problem Statement:
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

Algorithm:
1. Whitespace: Ignore leading whitespace (" ").
2. Signedness: Determine the sign by checking '-' or '+' (default positive).
3. Conversion: Read digits until a non-digit or end of string. Ignore leading zeros.
4. Rounding: Clamp the result to 32-bit signed integer range [-2^31, 2^31-1].
5. Return the integer.

---

### Example 1:
Input: s = "42"  
Output: 42

### Example 2:
Input: s = " -042"  
Output: -42

### Example 3:
Input: s = "1337c0d3"  
Output: 1337

### Example 4:
Input: s = "0-1"  
Output: 0

### Example 5:
Input: s = "words and 987"  
Output: 0

---

### Constraints:
- 0 <= s.length <= 200
- s consists of English letters (lower/upper case), digits, ' ', '+', '-', and '.'
"""

# 💡 Explanation:
# - Strip leading whitespace.
# - Determine the sign and adjust the string.
# - Read digits and form the number.
# - Apply sign and clamp within 32-bit signed integer range.

class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        if not s: 
            return 0

        sign = -1 if s[0] == '-' else 1
        if s[0] in '+-': 
            s = s[1:]

        num, i = 0, 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign
        return max(min(num, 2**31 - 1), -2**31)


"""
🎯 Practice Link:
https://leetcode.com/problems/string-to-integer-atoi/description/
"""
