class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        smallest_digit = nums[0]
        max_diff = 0

        for num in nums:
            smallest_digit = min(smallest_digit, num)
            max_diff = max(max_diff, num - smallest_digit)

        if max_diff == 0:
            max_diff = -1
        
        return max_diff