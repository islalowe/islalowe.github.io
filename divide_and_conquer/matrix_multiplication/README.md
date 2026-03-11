# Matrix Multiplication
Matrix multiiplication involves taking two 2D matrices and computing each entry of the result matrix by taking the **dot product of a row of the first matrix and a column of the second matrix**.

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
w & x \\
y & z
\end{pmatrix}
=
\begin{pmatrix}
aw + by & ax + bz \\
cw + dy & cx + dz
\end{pmatrix}
$$



## Problem
Given two matrices `A[][]` and `B[][]`, where `A` is an `m x n` matrix and B is a `n x p` matrix, compute `C = AB`. 
We must find the dot product.
The resulting matrix has dimensions `m x p`.

## Divide and Conquer Idea
Divide: partition A and B into `½n`-by-`½n` blocks.
Conquer: multiply the 8 submatrix products recursively.
Combine: Add the appropriate products to form the 4 quadrants of the result matrix.

Since the matrices in this implementation are square, with `n` x `n` dimensions where `n` is divisible by 2, we can use **Strassen's algorithm** to divide the matrix into submatrices, of size `(n/2)` × `(n/2)`.
After the raw matrices are divided into 8 submatrices, `A` - `H`, they need to be used for the dot matrix computation, which will produce new submatrices with Strassen's algorithm.
The submatrix products will be: 
$$
\begin{aligned}
S_1 &= A(F - H) \\
S_2 &= (A + B)H \\
S_3 &= (C + D)E \\
S_4 &= D(G - E) \\
S_5 &= (A + D)(E + H) \\
S_6 &= (B - D)(G + H) \\
S_7 &= (A - C)(E + F)
\end{aligned}
$$

## Implementation & Time Cmplexity
The running time `T(n)` is `T(n) = 7T(n/2) + kn^2`

## Pseudocode
```text
MatrixMultiplication(Matrix1, Matrix2):
    check len(Matrix1) == len(Matrix2)
    if len(Matrix1) == 1:
        return [[Matrix1[0][0] * Matrix2[0][0]]]

    partition Matrix1 into submatrices A, B, C, D
    partition Matrix2 into submatrices E, F, G, H

    S1 = MatrixMultiplication(A, F - H)
    S2 = MatrixMultiplication(A + B, H)
    S3 = MatrixMultiplication(C + D, E)
    S4 = MatrixMultiplication(D, G - E)
    S5 = MatrixMultiplication(A + D, E + H)
    S6 = MatrixMultiplication(B - D, G + H)
    S7 = MatrixMultiplication(A - C, E + F)

    I = S5 + S4 - S2 + S6
    J = S1 + S2
    K = S3 + S4
    L = S1 + S5 - S3 - S7

    combine I, J, K, L into one matrix Z

    return Z
```