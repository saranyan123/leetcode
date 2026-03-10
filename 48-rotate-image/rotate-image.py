class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        
 
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
   
        for i in range(n):
            matrix[i].reverse()

sol = Solution()
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(matrix1)
print("Example 1:", matrix1) 


matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(matrix2)
print("Example 2:", matrix2)

