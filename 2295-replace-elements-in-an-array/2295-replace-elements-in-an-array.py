class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        # Create a dictionary to map numbers to their indices in nums
        num_indices = {num: i for i, num in enumerate(nums)}
        
        # Iterate through operations
        for operation in operations:
            # Find the index of the number to replace
            replace_index = num_indices[operation[0]]
            # Replace the number at the index with the new number
            nums[replace_index] = operation[1]
            # Update the num_indices dictionary with the new number and index
            num_indices[operation[1]] = replace_index
            # Remove the old number from num_indices
            del num_indices[operation[0]]
        
        return nums