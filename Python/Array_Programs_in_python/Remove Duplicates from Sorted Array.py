"""
Problem : Remove Duplicates from Sorted Array

Problem Statement:
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Return the number of unique elements in nums.

You must do this without using extra space (O(1) extra memory).

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints:
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order
"""

# 💡 Explanation:
# Since the array is sorted, duplicates will always be adjacent.
# We can use two pointers:
#   - i: tracks the last unique element position
#   - j: scans the array
# Whenever nums[j] != nums[i], move i forward and update nums[i].
# Finally, return i + 1 (count of unique elements).

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1


"""
Practice Link:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array
"""
