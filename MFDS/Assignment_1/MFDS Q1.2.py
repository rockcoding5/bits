# Assignment from Batch : 108

# SHILOJU SHIVA KUMARACHARY
# VARUN KAMATH
# BALAJI N


# Q1.2 - Write a function to generate Gauss Seidel Iteration for a given square matrix. The function should also
# return the values of 1, ∞ and Frobenius norms of iteration matrix. Generate a random 4 × 4 matrix. Report the 
# Iteration matrix and its norm values returned by the function along with the input matrix.


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


# Function for gauss_seidel
def generate_gauss_seidel(A, b, tolerance=1e-10, max_iterations=10000):
    x = np.zeros_like(b, dtype=np.double)
    # print("x", str(x))

    # Iterate
    for k in range(max_iterations):
        # print("k ", str(k))

        x_old = x.copy()

        for i in range(A.shape[0] - 2):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, (i + 1):], x_old[(i + 1):])) / A[i, i]

        # Stop condition
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            break

    return x


A = rand_matrx
b = B
tolerance = 1e-10
max_iterations = 10

print("Tolerance: " + str(tolerance))
print("Max Iterations: " + str(max_iterations))

x_gauss_seidel = generate_gauss_seidel(A, b, tolerance, max_iterations)
print("x_gauss_seidel: " + str(x_gauss_seidel) + "\n")

# 1 Norm
one_norm = np.linalg.norm(x_gauss_seidel, ord=1)
print("1 Norm: " + str(one_norm) + "\n")

# Infinite Norm
inf_norm = norm(x_gauss_seidel, inf)
print("Infinite Norm: " + str(inf_norm) + "\n")

# Frobenius Norm
frob_norm = norm(x_gauss_seidel, 'fro')
print("Frobenius Norm: " + str(frob_norm) + "\n")
