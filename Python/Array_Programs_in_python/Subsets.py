"""
Problem : Subsets

📌 Problem Statement:
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

# 💡 Explanation:
# The task is to generate the power set of the given array (all subsets).
# We use backtracking:
#   - Start with an empty subset (path).
#   - At each step, either include the current number or skip it.
#   - Explore all possible combinations by recursive calls.
# This ensures we generate all subsets without duplicates.

class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, path):
            # Add current subset (copy of path)
            res.append(path[:])

            # Explore further elements
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


"""
🎯 Practice Link:
https://leetcode.com/problems/subsets/description/
"""
