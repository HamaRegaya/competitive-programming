class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxC = max(candies)
        a = [ n + extraCandies >= maxC for n in candies]
        return a