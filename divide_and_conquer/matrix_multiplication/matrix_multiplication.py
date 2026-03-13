# Helper function for Strassen's 7 compputations
def add_matrix(mat_a, mat_b):
    rows = len(mat_a)
    cols = len(mat_a[0])
    return [
        [mat_a[i][j] + mat_b[i][j] for j in range(cols)]
        for i in range(rows)
    ]

# Helper function for Strassen's 7 compputations on the quadrants
def subtract_matrix(mat_a, mat_b):
    rows = len(mat_a)                                              
    cols = len(mat_a[0])
    result = []   
    for i in range(rows):
        row = []                                                   
        # go through each column
        for j in range(cols):
            value = mat_a[i][j] - mat_b[i][j]
            row.append(value)
        result.append(row)
    return result

# Helper function to partition the matrix
def split_matrix(matrix):
    part = len(matrix) // 2
    A = [row[:part] for row in matrix[:part]]
    B = [row[part:] for row in matrix[:part]]
    C = [row[:part] for row in matrix[part:]]
    D = [row[part:] for row in matrix[part:]]
    return A, B, C, D

# Helper function to create the final result
# ex:  I = (93 79)       J = (110 115) 
#          (29 97)           (120 149)
def combine_matrices(I, J, K, L):
    result = []
    rows = len(I)                               # number of rows in each quadrant
    # I and J
    for i in range(rows):
        row = []
        # add elements from I
        for value in I[i]:
            row.append(value)
        # add elements from J
        for value in J[i]:
            row.append(value)
        result.append(row)
    # K and L
    for i in range(rows):
        row = []
        # add elements from K
        for value in K[i]:
            row.append(value)
        # add elements from L
        for value in L[i]:
            row.append(value)
        result.append(row)
    return result




# This is the main computation function, and it calls the helper functions
def multiply_matrix(mat_1, mat_2):
    # Check dimensions are compatible
    if len(mat_1[0]) != len(mat_2):
        print("Number of columns and rows in must be compatible")

    # Base case
    if len(mat_1) == 1:
        return [[mat_1[0][0] * mat_2[0][0]]]

    # Partition matrices into quadrants
    A, B, C, D = split_matrix(mat_1)
    E, F, G, H = split_matrix(mat_2)

    # Strassen's 7 recursive products
    S1 = multiply_matrix(A, subtract_matrix(F, H))                      # S_1 = A(F - H) 
    S2 = multiply_matrix(add_matrix(A, B), H)                           # S_2 = (A + B)H 
    S3 = multiply_matrix(add_matrix(C, D), E)                           # S_3 = (C + D)E 
    S4 = multiply_matrix(D, subtract_matrix(G, E))                      # S_4 = D(G - E)
    S5 = multiply_matrix(add_matrix(A, D), add_matrix(E, H))            # S_5 = (A + D)(E + H)
    S6 = multiply_matrix(subtract_matrix(B, D), add_matrix(G, H))       # S_6 = (B - D)(G + H)
    S7 = multiply_matrix(subtract_matrix(A, C), add_matrix(E, F))       # S_7 = (A - C)(E + F)

    # Compute result quadrants
    I = add_matrix(subtract_matrix(add_matrix(S5, S4), S2), S6)         # I = S5 + S4 - S2 + S6
    J = add_matrix(S1, S2)                                              # J = S1 + S2
    K = add_matrix(S3, S4)                                              # K = S3 + S4
    L = subtract_matrix(subtract_matrix(add_matrix(S1, S5), S3), S7)    # L = S1 + S5 - S3 - S7

    # Combine into final matrix
    return combine_matrices(I, J, K, L)


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
        [3, 6, 4, 6],
        [1, 4, 7, 9]
    ]

    result = multiply_matrix(mat_1, mat_2)

    print("Matrix 1:\n")
    for row in mat_1:
        print(row)
    print("\nMatrix 2:\n")
    for row in mat_2:
        print(row)

    print("\nResult matrix:\n")
    for row in result:
        print(row)
