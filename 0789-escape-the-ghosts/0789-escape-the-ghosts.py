class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        tab=[]
        
        for ghost in ghosts :
            x=abs(ghost[0]-target[0]) + abs(ghost[1]-target[1])
            tab.append(x)
            
        z=min(tab)
        y=abs(target[0])+abs(target[1])
        
        if y < z :
             return True
            
        else:
             return False