class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(1 <= n <= 150):
            if(n%2):
                return n*2
            else:
                return n