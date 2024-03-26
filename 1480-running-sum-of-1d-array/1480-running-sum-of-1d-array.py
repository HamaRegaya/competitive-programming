class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = 0
        result = []
        for num in nums:
            running_sum += num
            result.append(running_sum)
        return result
        