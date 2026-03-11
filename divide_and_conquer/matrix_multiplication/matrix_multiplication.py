# Function to add two matrices of same dimensions r×c
def add(mat_a, mat_b):
    a_len = len(mat_a)
    b_len = len(mat_b[0])

    # Initialize result matrix with dimensions r×c
    res = [[0] * c for _ in range(r)]

    # Perform element-wise addition
    for i in range(r):
        for j in range(c):
            res[i][j] = mat_a[i][j] + mat_b[i][j]

    return res

# Function to multiply mat1 (n×m) with mat2 (m×q)
def multiply(mat_a, mat_b):
    n = len(mat_a)
    m = len(mat_a[0])
    q = len(mat_b[0])

    # Initialize result matrix with dimensions n×q
    res = [[0] * q for _ in range(n)]

    # Matrix multiplication logic
    for i in range(n):
        for j in range(q):
            for k in range(m):
                res[i][j] += mat_a[i][k] * mat_b[k][j]

    return res
    
if __name__ == "__main__":
    mat_a = [
        [9, 8, 1, 2],
        [0, 7, 2, 9],
        [6, 4, 3, 5],
        [5, 2, 8, 6]
    ]
    
    mat_b = [
        [8, 1, 4, 3],
        [2, 7, 7, 8],
        [3, 6, 4, 6]
        [1, 4, 7, 9]
    ]

    
    res = multiply(mat_a, mat_b)
    
    for row in res:
        print(" ".join(map(str, row)))