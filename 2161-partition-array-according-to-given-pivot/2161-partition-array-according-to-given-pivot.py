class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        # Separate elements less than pivot, equal to pivot, and greater than pivot
        l = [num for num in nums if num < pivot]
        p = [num for num in nums if num == pivot]
        g = [num for num in nums if num > pivot]
        
        # Return the concatenation of the three lists
        return l + p + g