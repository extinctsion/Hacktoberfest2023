"""
 Problem : Largest Color Value in a Directed Graph

📌 Problem Statement:
Given a directed graph of n colored nodes and m edges:  
- nodes are numbered 0 to n-1.  
- colors[i] is a lowercase letter representing the color of node i.  
- edges[j] = [aj, bj] represents a directed edge from aj to bj.  

A valid path is a sequence of nodes where each consecutive pair has a directed edge.  
The color value of a path = number of nodes with the most frequent color in the path.  

Return the largest color value of any valid path, or -1 if the graph contains a cycle.

---

### Example 1:
Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]  
Output: 3  
Explanation: Path 0 → 2 → 3 → 4 contains 3 nodes colored "a".

### Example 2:
Input: colors = "a", edges = [[0,0]]  
Output: -1  
Explanation: There is a cycle from 0 to 0.

---

### Constraints:
- n == colors.length
- m == edges.length
- 1 <= n <= 10^5
- 0 <= m <= 10^5
- colors consists of lowercase English letters
- 0 <= aj, bj < n
"""

# 💡 Explanation:
# - Use topological sort (Kahn's algorithm) to detect cycles and process nodes in order.  
# - For each node, maintain color_count[node][c] = max count of color c along any path to this node.  
# - Propagate counts along edges and update max color value.  
# - If cycle exists (some nodes never visited), return -1.

class Solution(object):
    def largestPathValue(self, colors, edges):
        num_nodes = len(colors)
        adjacency_list = [[] for _ in range(num_nodes)]
        color_count = [[0] * 26 for _ in range(num_nodes)]
        indegree = [0] * num_nodes

        # Build graph
        for src, dest in edges:
            adjacency_list[src].append(dest)
            indegree[dest] += 1

        # Initialize queue with nodes having indegree 0
        queue = [node for node in range(num_nodes) if indegree[node] == 0]

        max_color_value = 0
        visited_nodes = 0

        while queue:
            next_queue = []
            for node in queue:
                visited_nodes += 1
                color_index = ord(colors[node]) - ord('a')
                color_count[node][color_index] += 1
                max_color_value = max(max_color_value, color_count[node][color_index])
                
                for neighbor in adjacency_list[node]:
                    for c in range(26):
                        color_count[neighbor][c] = max(color_count[neighbor][c], color_count[node][c])
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        next_queue.append(neighbor)
            queue = next_queue

        return max_color_value if visited_nodes == num_nodes else -1


"""
🎯 Practice Link:
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
"""
