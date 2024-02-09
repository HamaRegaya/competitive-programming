class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                if count > 1:
                    return False
                # If nums[i] is smaller than nums[i - 1],
                # we need to modify either nums[i] or nums[i - 1].
                # We prioritize modifying nums[i] if possible.
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
        
        return True
        