class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos_nums = [num for num in nums if num > 0]
        neg_nums = [num for num in nums if num < 0]
        
        # Initialize the result array
        result = []
        
        # Alternate placing positive and negative numbers
        for i in range(len(pos_nums)):
            result.append(pos_nums[i])
            result.append(neg_nums[i])
        
        return result