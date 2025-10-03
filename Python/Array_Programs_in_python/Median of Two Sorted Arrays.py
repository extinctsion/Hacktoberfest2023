"""
 Problem : Median of Two Sorted Arrays

📌 Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""

# 💡 Explanation:
# The naive approach is to merge both sorted arrays and then find the median.
# Steps:
#   1. Merge nums1 and nums2 into a single sorted array.
#   2. If length is odd -> return middle element.
#   3. If length is even -> return average of the two middle elements.
#
# This solution works but runs in O((m+n) log(m+n)) due to sorting.
# Optimal solutions exist with O(log(min(m,n))) using binary search,
# but this is the simpler approach.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            mid1 = merged[(n // 2) - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2.0


"""
🎯 Practice Link:
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""
