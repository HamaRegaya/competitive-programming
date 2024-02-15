class Solution:
    def twoSum(self, nums, target):
        num_index_map = {}  # Maps numbers to their indices
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_index_map:
                return [num_index_map[complement], i]
            num_index_map[num] = i
        return []