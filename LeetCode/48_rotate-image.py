"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
        
    # diagonal flip (axe = top left to bottom right) 
    for y in range(n):
        for x in range(y):
            temp = matrix[y][x] 
            matrix[y][x] = matrix[x][y]
            matrix[x][y] = temp
       
    # vertical flip
    for y in range(n):
        for x in range(n/2):
            temp = matrix[y][x] 
            matrix[y][x] = matrix[y][n-1-x]
            matrix[y][n-1-x] = temp
       
    return matrix

if __name__ == '__main__':
    A = [[1,2,3],
         [4,5,6],
         [7,8,9]]
        
    B = [[ 5, 1, 9,11],
         [ 2, 4, 8,10],
         [13, 3, 6, 7],
         [15,14,12,16]]

    print(rotate(A))
    print(rotate(B))
    