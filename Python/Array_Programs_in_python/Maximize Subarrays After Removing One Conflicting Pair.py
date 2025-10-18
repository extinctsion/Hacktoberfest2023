"""
 Problem : Maximize Subarrays After Removing One Conflicting Pair

📌 Problem Statement:
You are given an integer n which represents an array nums containing the numbers from 1 to n in order.  
Additionally, you are given a 2D array conflictingPairs, where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

You must remove exactly one element from conflictingPairs.  
Afterward, count the number of non-empty subarrays of nums which do not contain both a and b for any remaining conflicting pair [a, b].  

Return the maximum number of subarrays possible after removing exactly one conflicting pair.

---

### Example 1:
Input: 
n = 4, conflictingPairs = [[2,3],[1,4]]

Output: 
9

Explanation:
Remove [2, 3] from conflictingPairs.  
Now, conflictingPairs = [[1, 4]].  
There are 9 subarrays in nums where [1, 4] do not appear together.  
They are [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3] and [2, 3, 4].

---

### Example 2:
Input: 
n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]

Output: 
12

Explanation:
Remove [1, 2] from conflictingPairs.  
Now, conflictingPairs = [[2, 5], [3, 5]].  
There are 12 subarrays in nums where [2, 5] and [3, 5] do not appear together.

---

### Constraints:
- 2 <= n <= 10^5
- 1 <= conflictingPairs.length <= 2 * n
- conflictingPairs[i].length == 2
- 1 <= conflictingPairs[i][j] <= n
- conflictingPairs[i][0] != conflictingPairs[i][1]
"""

# 💡 Explanation:
# - We have to maximize valid subarrays by removing one conflicting pair.
# - For each right boundary "r", track left restrictions caused by conflicting pairs.
# - Keep track of the best removal "bonus" that maximizes valid subarray counts.
# - Finally return total valid subarrays + best bonus.
#
# Complexity: O(n + conflictingPairs.length)

class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        right = [[] for _ in range(n + 1)]

        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))

        ans = 0
        left = [0, 0]  
        bonus = [0] * (n + 1)

        for r in range(1, n + 1):
            for l in right[r]:
                left = self.maxPair(left, [l, left[0]], [left[0], l])
            ans += r - left[0]
            bonus[left[0]] += left[0] - left[1]

        return ans + max(bonus)

    def maxPair(self, pair1, pair2, pair3):
        max_pair = pair1
        for curr in [pair2, pair3]:
            if curr[0] > max_pair[0] or (curr[0] == max_pair[0] and curr[1] > max_pair[1]):
                max_pair = curr
        return max_pair


"""
🎯 Practice Link:
https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/description/
"""
