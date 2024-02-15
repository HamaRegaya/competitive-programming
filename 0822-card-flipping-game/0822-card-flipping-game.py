class Solution:
    def flipgame(self, fronts, backs):
        n = len(fronts)
        good_integers = set()
        
        for i in range(n):
            if fronts[i] == backs[i]:
                good_integers.add(fronts[i])
        
        min_good = float('inf')
        for num in fronts + backs:
            if num not in good_integers:
                min_good = min(min_good, num)
        
        return min_good if min_good != float('inf') else 0