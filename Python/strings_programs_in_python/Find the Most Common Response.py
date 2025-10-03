"""
Problem : Find the Most Common Response

📌 Problem Statement:
You are given a 2D string array `responses` where each `responses[i]` is an array of strings representing survey responses from the ith day.

Return the most common response across all days after removing duplicate responses within each `responses[i]`.  
If there is a tie, return the lexicographically smallest response.

---

### Example 1:
Input: responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]  
Output: "good"

Explanation:
After removing duplicates within each list:
[["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]].  
Frequencies: "good"=3, "ok"=2, "bad"=2 → Return "good".

### Example 2:
Input: responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]  
Output: "bad"

Explanation:
After removing duplicates:
[["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]].  
Frequencies: "bad"=2, "good"=2, "ok"=2 → Return lexicographically smallest: "bad".

---

### Constraints:
- 1 <= len(responses), len(responses[i]) <= 10^4
- Each string consists of lowercase English letters
"""

# 💡 Explanation:
# - For each day, remove duplicate responses using a set.
# - Count each unique response across all days.
# - Find responses with highest frequency.
# - Return the lexicographically smallest if multiple responses tie.

from collections import Counter

class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        freq_counter = Counter()
        for daily_responses in responses:
            unique_responses = set(daily_responses)
            for response in unique_responses:
                freq_counter[response] += 1
        
        highest_frequency = max(freq_counter.values())
        candidates = [response for response, frequency in freq_counter.items() if frequency == highest_frequency]
        return min(candidates)


"""
🎯 Practice Link:
https://leetcode.com/problems/find-the-most-common-response/description/
"""
