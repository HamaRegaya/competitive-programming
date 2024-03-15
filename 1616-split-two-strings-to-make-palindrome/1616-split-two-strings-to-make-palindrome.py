class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.inner_check(a, b) or self.inner_check(b, a)
    
    def inner_check(self, a: str, b: str) -> bool:
        left, right = 0, len(a) - 1
        
        ab_possible, aa_possible, bb_possible = True, True, True
        while left <= right and (ab_possible or aa_possible or bb_possible):
            aa_possible = (ab_possible or aa_possible) and a[left] == a[right]
            bb_possible = (ab_possible or bb_possible) and b[left] == b[right]
            ab_possible = ab_possible and a[left] == b[right]
            left, right = left + 1, right - 1
            
        return aa_possible or ab_possible or bb_possible
