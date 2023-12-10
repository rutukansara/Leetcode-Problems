import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # also tried doing [[0]*3]*3
        # realized that cannot be done because it does something called shallow copy
        # shallow copy - [[0]*3]*3 multiplies the list thrice, which means when one row is changed, the same change will happen in all the rows - we dont want that
    
        transposed_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposed_matrix[j][i] = matrix[i][j]
        return transposed_matrix