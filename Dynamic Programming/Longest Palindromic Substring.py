"""
Problem: Longest Palindromic Substring

📌 Problem Statement:
Given a string `s`, return the longest palindromic substring in `s`.

---

### Example 1:
Input: s = "babad"  
Output: "bab"  
Explanation: "aba" is also a valid answer.

### Example 2:
Input: s = "cbbd"  
Output: "bb"

---

### Constraints:
- 1 <= s.length <= 1000
- s consists of only digits and English letters
"""

# 💡 Explanation:
# - Use "expand around center" approach.
# - For each index, consider odd-length and even-length palindromes.
# - Expand as long as characters match.
# - Track start index and max length of longest palindrome.

class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        start, max_length = 0, 0

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            # Odd length palindrome
            l1, r1 = expand_around_center(i, i)  
            # Even length palindrome
            l2, r2 = expand_around_center(i, i + 1)  

            if r1 - l1 > max_length:
                start, max_length = l1, r1 - l1
            if r2 - l2 > max_length:
                start, max_length = l2, r2 - l2

        return s[start:start + max_length + 1]


"""
🎯 Practice Link:
https://leetcode.com/problems/longest-palindromic-substring/description/
"""
