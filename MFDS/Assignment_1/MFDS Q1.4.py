# Assignment from Batch : 108

# SHILOJU SHIVA KUMARACHARY
# VARUN KAMATH
# BALAJI N


# Q1.4 - Write a function that perform Gauss Seidel iterations. Generate a random 4 × 4 matrix A and generate a
# random b ∈ R^4 Report the results of passing this matrix to function written in (i). Solve linear system Ax = b by
# using function in (ii). Generate a plot of ∥xk+1 − xk∥2 for first 100 iterations. Does it converge ? or Is it
# diverging? Specify your observation. Take a screenshot of plot and paste it in the assignment document.


import numpy as np
from numpy import inf
from numpy.linalg import norm
import matplotlib.pyplot as plt

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


# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix

def generate_gauss_seidel(a, x, b):
    # Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if j != i:
                d = d.astype('float64')
                d -= a[j][i] * x[i]

        # updating the value of our solution
        x[j] = d / a[j][j]
    # returning our updated solution
    return x


# int(input())input as number of variable to be solved
n = 100  # As mention in problem statement
a = rand_matrx
b = B
# initial solution depending on n(here n=3)
x = np.ones((4, 1), dtype=int)

print("Number of Iterations: " + str(n))
print("x: " + str(x) + "\n")

# loop run for m times depending on m the error value
for i in range(0, n - 1):
    x = generate_gauss_seidel(a, x, b)
    # print each time the updated solution
    if i in range(0, 10):
        print("Iteration " + str(i+1) + ": " + str(x) + "\n")

print("After 100 Iterations, x: " + str(x) + "\n")

plt.plot(x)
plt.show()
