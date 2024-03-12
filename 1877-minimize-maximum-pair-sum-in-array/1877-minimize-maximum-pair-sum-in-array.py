class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()  # Sorting the array to pair smallest with largest
        n = len(nums)
        left, right = 0, n - 1
        max_pair_sum = float('-inf')

        while left < right:
            pair_sum = nums[left] + nums[right]
            max_pair_sum = max(max_pair_sum, pair_sum)
            left += 1
            right -= 1

        return max_pair_sum
