class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        table={}
        answer0=[]
        answer1=[]
        
        for play in matches:
            if play[0] in table:
                table[play[0]][0]+=1
            else:
                table[play[0]]=[1,0]
            if play[1] in table:
                table[play[1]][1]+=1
            else: 
                table[play[1]]=[0,1]
        for item in table:
            if table[item][0]>0 and  table[item][1]==0:
                answer0.append(item)
            if table[item][1]==1:
                answer1.append(item)
        return [sorted(answer0),sorted(answer1)]

        not_lost.sort()
        lost_once.sort()

        return [not_lost, lost_once]