class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])

        o = [[None] * r for _ in range(c)]
        
        for i in range(c):
            for j in range(r):
                o[i][j] = matrix[j][i]

        return o
        