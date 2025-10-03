"""
 Problem : Kth Smallest Product of Two Sorted Arrays

📌 Problem Statement:
Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, 
return the kth (1-based) smallest product of nums1[i] * nums2[j] 
where 0 <= i < nums1.length and 0 <= j < nums2.length.

Example 1:
Input: nums1 = [2,5], nums2 = [3,4], k = 2
Output: 8
Explanation:
Products = [6, 8, 15, 20]
The 2nd smallest product is 8.

Example 2:
Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
Output: 0
Explanation:
The 6 smallest products are [-16, -8, -8, -4, 0, 0]
The 6th smallest product is 0.

Example 3:
Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
Output: -6
Explanation:
The 3 smallest products are [-10, -8, -6]
The 3rd smallest product is -6.

Constraints:
1 <= nums1.length, nums2.length <= 5 * 10^4
-10^5 <= nums1[i], nums2[j] <= 10^5
1 <= k <= nums1.length * nums2.length
nums1 and nums2 are sorted.
"""

# 💡 Explanation:
# The brute force approach (generating all products and sorting) is impossible 
# due to size (up to 2.5 * 10^9 elements).
#
# Efficient Approach:
# - Use Binary Search on the possible product values (range: [-1e10, 1e10]).
# - For each candidate mid, count how many products <= mid using two pointers + binary search.
# - If count >= k → shrink right bound, else move left bound up.
# - Final answer will be the smallest number where count >= k.
#
# Complexity: O((m+n) * log(max_val)) with binary search.

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        import bisect

        def leq(x):
            """Count how many products <= x"""
            count = 0
            for i in nums1:
                if i > 0:
                    count += bisect.bisect_right(nums2, x // i)
                elif i < 0:
                    count += len(nums2) - bisect.bisect_left(nums2, -(-x // i))
                else:  # i == 0
                    if x >= 0:
                        count += len(nums2)
            return count

        # Ensure nums1 is the smaller one (optimization)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        left, right = -10 ** 10, 10 ** 10  # search space

        while left < right:
            mid = (left + right) // 2
            if leq(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left


"""
🎯 Practice Link:
https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/description/
"""
