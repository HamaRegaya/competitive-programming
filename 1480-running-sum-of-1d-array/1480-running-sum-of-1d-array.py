class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        T=[]
        sum=0
        for i in nums:
            sum += i
            T.append(sum)
        return T