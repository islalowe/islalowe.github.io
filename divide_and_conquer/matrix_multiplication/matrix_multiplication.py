# # Function to add two matrices of same dimensions r×c
# def add(mat_a, mat_b):
#     a_len = len(mat_a)
#     b_len = len(mat_b[0])
    

#     # Initialize result matrix with dimensions r×c
#     res = [[0] * c for _ in range(r)]

#     # Perform element-wise addition
#     for i in range(r):
#         for j in range(c):
#             res[i][j] = mat_a[i][j] + mat_b[i][j]

#     return res

# # Function to multiply mat1 (n×m) with mat2 (m×q)
# def multiply(mat_a, mat_b):
#     n = len(mat_a)
#     m = len(mat_a[0])
#     q = len(mat_b[0])

#     if (a_len == b_len): 
#         continue

#     # Initialize result matrix with dimensions n×q
#     res = [[0] * q for _ in range(n)]

#     # Matrix multiplication logic
#     for i in range(n):
#         for j in range(q):
#             for k in range(m):
#                 res[i][j] += mat_a[i][k] * mat_b[k][j]

#     return res

    
#     res = multiply(mat_a, mat_b)
    
#     for row in res:
#         print(" ".join(map(str, row)))



def matrix_multiply(mat_1, mat_2):
    # mat_1 had dimensions m x n
    # mat_2 has dimensions n x p
    # the number of columns in Matrix1 must match the number of rows in Matrix2
    len(mat_1[0]) == len(mat_2)
    
     
#     if len(Matrix1) == 1:
#         return [[Matrix1[0][0] * Matrix2[0][0]]]

#     partition Matrix1 into submatrices A, B, C, D
#     partition Matrix2 into submatrices E, F, G, H

#     S1 = MatrixMultiplication(A, F - H)
#     S2 = MatrixMultiplication(A + B, H)
#     S3 = MatrixMultiplication(C + D, E)
#     S4 = MatrixMultiplication(D, G - E)
#     S5 = MatrixMultiplication(A + D, E + H)
#     S6 = MatrixMultiplication(B - D, G + H)
#     S7 = MatrixMultiplication(A - C, E + F)

#     I = S5 + S4 - S2 + S6
#     J = S1 + S2
#     K = S3 + S4
#     L = S1 + S5 - S3 - S7

#     combine I, J, K, L into one matrix Z
    return mat_3




if __name__ == "__main__":
    mat_1 = [
        [9, 8, 1, 2],
        [0, 7, 2, 9],
        [6, 4, 3, 5],
        [5, 2, 8, 6]
    ]
    mat_2 = [
        [8, 1, 4, 3],
        [2, 7, 7, 8],
        [3, 6, 4, 6]
        [1, 4, 7, 9]
    ]