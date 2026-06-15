2016. Maximum Difference Between Increasing Elements
Problem Statement

Given a 0-indexed integer array nums, find the maximum difference between nums[i] and nums[j] such that:

0 <= i < j < n
nums[i] < nums[j]

Return the maximum difference nums[j] - nums[i].

If no such pair exists, return -1.

Examples
Example 1
Input: nums = [7,1,5,4]
Output: 4

Explanation:

Buy at 1
Sell at 5
Difference = 5 - 1 = 4
Example 2
Input: nums = [9,4,3,2]
Output: -1

Explanation:

The array is strictly decreasing, so no valid pair exists.

Example 3
Input: nums = [1,5,2,10]
Output: 9

Explanation:

Buy at 1
Sell at 10
Difference = 10 - 1 = 9
Approach

The problem is very similar to Best Time to Buy and Sell Stock.

We maintain:

min_num → smallest value seen so far
max_diff → maximum valid difference found so far

For every element:

Calculate the difference between the current number and the smallest number seen before it.
Update the maximum difference if the current difference is larger.
Update the smallest number if the current element is smaller.

This ensures that:

i < j is always satisfied.
We only scan the array once.

Dry Run

For:

nums = [7,1,5,4]
Current Number	Minimum So Far	Difference	Max Difference
1	7 → 1	-	-1
5	1	4	4
4	1	3	4

Final Answer:

4
Complexity Analysis
Complexity	Value
Time	O(n)
Space	O(1)
Time Complexity

O(n) because we traverse the array only once.

Space Complexity

O(1) since only a few variables are used.

Key Concepts
Array Traversal
Greedy Approach
Running Minimum
Single Pass Optimization
Similar to "Best Time to Buy and Sell Stock"
