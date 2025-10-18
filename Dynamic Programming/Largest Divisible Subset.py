"""
Problem : Largest Divisible Subset

📌 Problem Statement:
Given a set of distinct positive integers `nums`, return the largest subset `answer` such that every pair (answer[i], answer[j]) satisfies:

- answer[i] % answer[j] == 0, or
- answer[j] % answer[i] == 0

If multiple solutions exist, return any of them.

---

### Example 1:
Input: nums = [1,2,3]  
Output: [1,2]  
Explanation: [1,3] is also accepted.

### Example 2:
Input: nums = [1,2,4,8]  
Output: [1,2,4,8]

---

### Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 2 * 10^9
- All integers in nums are unique
"""

# 💡 Explanation:
# - Sort nums to ensure if nums[i] % nums[j] == 0, nums[i] > nums[j].
# - Use DP:
#     - dp[i] = length of largest divisible subset ending at nums[i]
#     - prev[i] = previous index in the subset
# - Track maximum dp value and its index.
# - Reconstruct the subset from prev array.

class Solution(object):
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n

        max_size = 1
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        return result[::-1]


"""
🎯 Practice Link:
https://leetcode.com/problems/largest-divisible-subset/description/
"""
