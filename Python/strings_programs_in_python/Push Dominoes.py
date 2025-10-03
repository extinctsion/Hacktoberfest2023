"""
Problem : Push Dominoes

📌 Problem Statement:
There are n dominoes in a line, initially upright. Some dominoes are pushed to the left 'L' or right 'R', others remain '.'.

Rules:
- Each second, falling dominoes push adjacent dominoes in the same direction.
- Dominoes falling from both sides remain upright.
- Dominoes falling expend no additional force to already fallen dominoes.

Given a string `dominoes`, return the final state after all dominoes have fallen.

---

### Example 1:
Input: dominoes = "RR.L"  
Output: "RR.L"  
Explanation: First domino does not push the second domino further.

### Example 2:
Input: dominoes = ".L.R...LR..L.."  
Output: "LL.RR.LLRRLL.."

---

### Constraints:
- n == dominoes.length
- 1 <= n <= 10^5
- dominoes[i] is either 'L', 'R', or '.'
"""

# 💡 Explanation:
# - Use a forces array to track net force on each domino.
# - First pass left to right, assign positive force from 'R' pushes.
# - Second pass right to left, subtract force from 'L' pushes.
# - Convert net force to final state:
#     - f > 0 → 'R', f < 0 → 'L', f = 0 → '.'

class Solution(object):
    def pushDominoes(self, dominoes):
        n = len(dominoes)
        forces = [0] * n

        # Left to right
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # Right to left
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # Generate final state
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return ''.join(result)


"""
🎯 Practice Link:
https://leetcode.com/problems/push-dominoes/description/
"""
