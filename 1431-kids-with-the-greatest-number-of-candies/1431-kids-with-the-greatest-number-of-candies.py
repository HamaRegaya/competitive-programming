class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxC = max(candies)
        ans = [ num + extraCandies >= maxC for num in candies]
        return ans