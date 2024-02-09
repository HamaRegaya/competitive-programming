class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = nums[:n]  # First half of nums
        y = nums[n:]  # Second half of nums
        
        result = []
        for i in range(n):
            result.append(x[i])
            result.append(y[i])
        
        return result
        