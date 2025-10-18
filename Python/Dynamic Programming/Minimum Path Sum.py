"""
 Problem: Minimum Path Sum

📌 Problem Statement:
Given an m x n grid filled with non-negative numbers, find a path from top-left to bottom-right which minimizes the sum of all numbers along its path.  
You can only move either down or right at any point.

---

### Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]  
Output: 7  
Explanation: Path 1 → 3 → 1 → 1 → 1 minimizes the sum.

### Example 2:
Input: grid = [[1,2,3],[4,5,6]]  
Output: 12

---

### Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200
"""

# 💡 Explanation:
# - Use Dynamic Programming (DP) to store minimum path sum to each cell.
# - DP[i][j] = grid[i][j] + min(DP[i-1][j], DP[i][j-1])
# - Fill the first row and first column separately since they have only one direction.
# - Return DP[m-1][n-1].

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # Initialize first row
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        # Initialize first column
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]


"""
🎯 Practice Link:
https://leetcode.com/problems/minimum-path-sum/description/
"""
