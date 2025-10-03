"""
📝 Problem: Zigzag Conversion

📌 Problem Statement:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows.  
For example, for numRows = 3:

P   A   H   N
A P L S I I G
Y   I   R

Reading line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

Function signature: string convert(string s, int numRows);

---

### Example 1:
Input: s = "PAYPALISHIRING", numRows = 3  
Output: "PAHNAPLSIIGYIR"

### Example 2:
Input: s = "PAYPALISHIRING", numRows = 4  
Output: "PINALSIGYAHRPI"

Explanation for numRows = 4:

P     I    N  
A   L S  I G  
Y A   H R  
P     I  

### Example 3:
Input: s = "A", numRows = 1  
Output: "A"

---

### Constraints:
- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'
- 1 <= numRows <= 1000
"""

# 💡 Explanation:
# - We simulate the zigzag writing by keeping track of current row and step (direction).
# - Append characters to each row.
# - Switch direction when we reach top or bottom.
# - Finally, concatenate all rows to get the final converted string.

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for _ in range(numRows)]
        index, step = 0, 1

        for char in s:
            rows[index].append(char)
            index += step
            if index == 0 or index == numRows - 1:
                step *= -1

        return "".join("".join(row) for row in rows)


"""
🎯 Practice Link:
https://leetcode.com/problems/zigzag-conversion/description/
"""
