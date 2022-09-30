class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        f1, f2 = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                f1 = True; break

        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                f2 = True; break

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = True
                    matrix[i][0] = True

        for i in range(1, len(matrix)):
            if matrix[i][0] is True:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        for i in range(1, len(matrix[0])):
            if matrix[0][i] is True:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        if f1: 
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if f2: 
            for i in range(len(matrix[0])):
                matrix[0][i] = 0 
        return
        
