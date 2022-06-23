#!/usr/bin/env python
# coding: utf-8

# In[102]:


# Assignment from Batch # 287 - 

# Dheeraj Tuteja -
# Manikandana -
# Deepak -


# In[103]:


# Q1.2 - Write a function to generate Gauss Seidel Iteration for a given square matrix. The function should also 
# return the values of 1, ∞ and Frobenius norms of iteration matrix. Generate a random 4 × 4 matrix. Report the 
# Iteration matrix and its norm values returned by the function along with the input matrix.


# In[104]:


# import numpy
import numpy as np
from numpy import array, inf
from numpy.linalg import norm
from scipy.linalg import solve

# In[113]:


# Generate Random Matrix

RandomMatrix = np.random.randint(10, size=(4, 4))
# Assumption for creating a matrix : Random log will choose integers between 1 an 10.
# Size of the Matrix is given in the problem statement 4 X 4 

print(RandomMatrix)  # Print Array (matrix)

B = np.random.randint(10, size=(4, 1))  # AX = B (RHS)
print((B))  # Print Array (matrix)


# In[114]:


# Function to check diagonally dominant
def IsDiagonallyDominant(MyMatrix):
    D = np.diag(np.abs(MyMatrix))  # Find diagonal coefficients
    S = np.sum(np.abs(MyMatrix), axis=1) - D  # Find row sum without diagonal
    if np.all(D > S):
        print('matrix is diagonally dominant')
    else:
        print('NOT diagonally dominant')
    return


# In[115]:


# Call the function and pass the numpy array (matrix)
IsDiagonallyDominant(RandomMatrix)


# In[116]:


# Function for gauss_seidel

def gauss_seidel(A, b, tolerance=1e-10, max_iterations=10000):
    x = np.zeros_like(b, dtype=np.double)
    print("x", str(x))

    # Iterate
    for k in range(max_iterations):
        print("k ", str(k))

        x_old = x.copy()
        #
        # print("A" + str(A))
        # print("b" + str(b))
        # print("x" + str(x))
        # Loop over rows
        for i in range(A.shape[0] -2):
            print("testing.... ", str(i))
            # print(A[:i])
            # print(A[i:])
            x1 = x[:i]
            print(x1)
            # print(x[i:])
            # print(".....")
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, (i + 1):], x_old[(i + 1):])) / A[i, i]
            print(x[:i])

        # Stop condition
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            break

    return x


# In[117]:


A = RandomMatrix
b = B
tolerance = 1e-10
max_iterations = 10

print("is it printing.....................................")
print(RandomMatrix)
print(B)
print(tolerance)
print(max_iterations)

# In[118]:


gauss_seidel(A, b, tolerance, max_iterations)

# In[119]:


# 1 Norm
print(np.linalg.norm(B, ord=1))

# In[120]:


# Infinite form
infintie_norm_of_B = norm(B, inf)
print(infintie_norm_of_B)

# In[121]:


# Frobenius form
frobenius_norm_of_B = norm(B, 'fro')
print(frobenius_norm_of_B)
