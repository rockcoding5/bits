# Assignment from Batch : 108

# SHILOJU SHIVA KUMARACHARY
# VARUN KAMATH
# BALAJI N

# Q1.3 - Write a function to generate Gauss Jacobi iteration for a given square matrix. The function should also 
# return the values of 1, ∞ and Frobenius norms of iteration matrix. Generate a random 4 × 4 matrix. Report the 
# Iteration matrix and its norm values returned by the function along with the input matrix.

# (Repeat part (ii) for the Gauss Jacobi iteration)


import numpy as np
from numpy import inf
from numpy.linalg import norm

# Generate Random Matrix

rand_matrx = np.random.randint(10, size=(4, 4))
# Assumption for creating a matrix : Random log will choose integers between 1 an 10.
# Size of the Matrix is given in the problem statement 4 X 4 

print("Random Matrix 4*4:\n" + str(rand_matrx) + "\n")

B = np.random.randint(10, size=(4, 1))  # AX = B (RHS)
print("B Matrix 4*1:\n" + str(B) + "\n")


# Function to check diagonally dominant
def check_diagonal_dominant_matrix(matrix):
    D = np.diag(np.abs(matrix))  # Find diagonal coefficients
    S = np.sum(np.abs(matrix), axis=1) - D  # Find row sum without diagonal
    if np.all(D > S):
        return True
    else:
        return False


# Call the function and pass the numpy array (matrix)
# Check given matrix is diagonal_dominant_matrix or not
if check_diagonal_dominant_matrix(matrix=rand_matrx):
    print("The matrix is a diagonally dominant matrix\n")
else:
    print("The matrix is not a diagonally dominant matrix\n")


def generate_jacobi(A, b, x, n):
    D = np.diag(A)
    R = A - np.diagflat(D)
    for i in range(n):
        x = (b - np.dot(R, x)) / D
    return x


A = rand_matrx
b = B
n = 25
x = np.ones((4, 4))


print("Number of Iterations: " + str(n))
print("x: " + str(x) + "\n")

x_jacobi = generate_jacobi(A, b, x, n)
print("x_jacobi : " + str(x_jacobi) + "\n")

# 1 Norm
one_norm = np.linalg.norm(x_jacobi, ord=1)
print("1 Norm: " + str(one_norm) + "\n")

# Infinite Norm
inf_norm = norm(x_jacobi, inf)
print("Infinite Norm: " + str(inf_norm) + "\n")

# Frobenius Norm
frob_norm = norm(x_jacobi, 'fro')
print("Frobenius Norm: " + str(frob_norm) + "\n")
