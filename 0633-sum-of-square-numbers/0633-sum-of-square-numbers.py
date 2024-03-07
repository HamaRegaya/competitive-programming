class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left, right = 0, int(math.sqrt(c))
    
        while left <= right:
            total = left * left + right * right
            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1

        return False
        