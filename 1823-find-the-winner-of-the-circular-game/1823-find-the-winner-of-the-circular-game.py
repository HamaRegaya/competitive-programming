class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        c = 0
        friends = list(range(1, n+1))
        while len(friends) != 1:
            j = (c + k - 1) % len(friends)
            friends.pop(j)
            c = j
        return friends[0]
        