class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        c=str(x)
        return (c==c[::-1])
        