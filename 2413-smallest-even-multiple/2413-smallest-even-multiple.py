class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if(1 <= n <= 150):
            if(n%2==0):
                return n
            else:
                return n*2
        