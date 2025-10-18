"""
📝 Problem : Minimum Deletions to Make String K-Special

📌 Problem Statement:
You are given a string `word` and an integer `k`.

We consider `word` to be k-special if 
|freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string, 
where freq(x) denotes the frequency of character x in word.

Return the minimum number of characters you need to delete to make `word` k-special.

---

### Example 1:
Input: word = "aabcaba", k = 0  
Output: 3  
Explanation: Delete 2 occurrences of "a" and 1 occurrence of "c" to make all frequencies equal.

### Example 2:
Input: word = "dabdcbdcdcd", k = 2  
Output: 2  
Explanation: Delete 1 occurrence of "a" and 1 occurrence of "d" to satisfy k-special condition.

### Example 3:
Input: word = "aaabaaa", k = 2  
Output: 1  
Explanation: Delete 1 occurrence of "b" to satisfy k-special condition.

---

### Constraints:
- 1 <= word.length <= 10^5
- 0 <= k <= 10^5
- word consists only of lowercase English letters
"""

# 💡 Explanation:
# - Count the frequency of each character.
# - Sort frequencies.
# - Try every frequency as a "target":
#     - Delete all characters less than target.
#     - Reduce characters greater than target+k to fit in the k range.
# - Keep track of minimum deletions across all targets.

from collections import Counter

class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        freq = Counter(word)
        freq_values = list(freq.values())
        freq_values.sort()

        min_deletions = float('inf')

        for i in range(len(freq_values)):
            target = freq_values[i]
            deletions = 0
            for f in freq_values:
                if f > target + k:
                    deletions += f - (target + k)
                elif f < target:
                    deletions += f  # remove all of it
            min_deletions = min(min_deletions, deletions)

        return min_deletions


"""
🎯 Practice Link:
https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/description/
"""
