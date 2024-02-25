class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        m = len(mat)
        n = len(mat[0])
        matrix_dic = {}

        for id_x in range(m):
            for id_y in range(n):
                if id_x + id_y not in matrix_dic:
                    matrix_dic[id_x + id_y] = [mat[id_x][id_y]]
                else:
                    matrix_dic[id_x + id_y].append((mat[id_x][id_y]))

        for m in matrix_dic.items():
            if m[0] % 2 == 0:
                [output.append(element) for element in m[1][::-1]]
            else:
                [output.append(element) for element in m[1]]

        return output
        