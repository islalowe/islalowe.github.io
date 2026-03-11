# Matrix Multiplication
Matrix multiiplication involves taking two 2D matrices and computing each entry of the result matrix by taking the dot product of a row of the first matrix with a column of the second matrix. The matrices must be the same size.

The **dot product** computes the sum of products of corresponding elements between rows of one matrix and columns of a second matrix.

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

## Implementation & Time Cmplexity
The time complexity is 

## Pseudocode
```text

```