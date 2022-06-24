# Assignment from Batch : 108

# SHILOJU SHIVA KUMARACHARY
# VARUN KAMATH
# BALAJI N


# Q1.5 - Write a function that perform  Gauss Jacobi iterations. Generate a random 4 × 4 matrix A and generate a
# random b ∈ R^4 Report the results of passing this matrix to function written in (i). Solve linear system Ax = b by
# using function in (ii). Generate a plot of ∥xk+1 − xk∥2 for first 100 iterations. Does it converge ? or Is it
# diverging? Specify your observation. Take a screenshot of plot and paste it in the assignment document.

# Repeat part (iv) for the Gauss Jacobi iteration


import matplotlib.pyplot as plt
import numpy as np
from numpy import zeros, diag, diagflat, dot

np.seterr(divide='ignore', invalid='ignore')

# Generate Random Matrix

rand_matrx = np.random.randint(100, size=(4, 4))
# Assumption for creating a matrix : Random log will choose integers between 1 an 10.
# Size of the Matrix is given in the problem statement 4 X 4

print("Random Matrix 4*4:\n" + str(rand_matrx) + "\n")

B = np.random.randint(100, size=(4, 1))  # AX = B (RHS)
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


# Solves the equation Ax=b via the Jacobi iterative method
def generate_jacobi(A, b, N=99, x=None):

    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(N):
        x = x.astype('float64')
        x = (b - dot(R, x)) / D
    return x


# int(input())input as number of variable to be solved
A = rand_matrx
b = B
N = 99
# initial solution depending on n(here n=3)
x = np.ones((4, 1), dtype=int)

print("N:" + str(N))


x_jacobi = generate_jacobi(A, b, N, x)
print("x_jacobi : " + str(x_jacobi) + "\n")

plt.plot(x_jacobi)
# plt.yscale('log')
plt.show()
