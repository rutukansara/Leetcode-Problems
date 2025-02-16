class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1

        while l < r:
            for i in range(r-l):
                top, bottom = l, r
                
                topLeft = matrix[top][l + i]

                # bottomLeft
                matrix[top][l + i] = matrix[bottom - i][l]

                # bottomRight
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # topRight
                matrix[bottom][r - i] = matrix[top + i][r]

                # topLeft
                matrix[top + i][r] = topLeft
            
            l += 1
            r -= 1