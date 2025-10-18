"""
 Problem: Triangle

📌 Problem Statement:
Given a triangle array, return the minimum path sum from top to bottom.  

- For each step, you may move to an adjacent number in the row below.  
- If you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

---

### Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]  
Output: 11  
Explanation: Path 2 → 3 → 5 → 1 = 11

### Example 2:
Input: triangle = [[-10]]  
Output: -10

---

### Constraints:
- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -10^4 <= triangle[i][j] <= 10^4

Follow up: Solve using only O(n) extra space, where n = number of rows.
"""

# 💡 Explanation:
# - Use bottom-up Dynamic Programming (DP).
# - Start from second-last row and add the minimum of two adjacent numbers from the row below.
# - Continue until top row contains the minimum total path sum.

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Start from the second-last row
        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])
        return triangle[0][0]


"""
🎯 Practice Link:
https://leetcode.com/problems/triangle/description/
"""
