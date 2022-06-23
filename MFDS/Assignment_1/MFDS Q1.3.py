#!/usr/bin/env python
# coding: utf-8

# In[64]:


# Assignment from Batch # 287 - 

#Dheeraj Tuteja -
#Manikandana - 
#Deepak -


# In[65]:


# Q1.3 - Write a function to generate Gauss Jacobi iteration for a given square matrix. The function should also 
# return the values of 1, ∞ and Frobenius norms of iteration matrix. Generate a random 4 × 4 matrix. Report the 
# Iteration matrix and its norm values returned by the function along with the input matrix.

#(Repeat part (ii) for the Gauss Jacobi iteration)


# In[66]:


#import numpy
import numpy as np
from numpy import array,inf
from numpy.linalg import norm 
from scipy.linalg import solve


# In[67]:


# Generate Random Matrix

RandomMatrix = np.random.randint(10, size=(4, 4)) 
# Assumption for creating a matrix : Random log will choose integers between 1 an 10.
# Size of the Matrix is given in the problem statement 4 X 4 

print((RandomMatrix)) #Print Array (matrix)
print(type(RandomMatrix)) #Print type of the array
print(RandomMatrix.shape) #Print shape of the array

B = np.random.randint(10, size=(4, 1)) # AX = B (RHS)
print((B)) #Print Array (matrix)
print(type(B)) #Print type of the array
print(B.shape) #Print shape of the array


# In[75]:


# Funnction to check diagonally dominant
def IsDiagonallyDominant(MyMatrix):
    D = np.diag(np.abs(MyMatrix)) # Find diagonal coefficients
    S = np.sum(np.abs(MyMatrix), axis=1) - D # Find row sum without diagonal
    if np.all(D > S):
        print ('matrix is diagonally dominant')
    else:
        print ('NOT diagonally dominant')
    return


# In[76]:


#Call the function and pass the numpy array (matrix)
IsDiagonallyDominant(RandomMatrix)


# In[77]:


def jacobi(A,b,x,n):
  D=np.diag(A)
  R=A-np.diagflat(D)
  for i in range(n):
    x=(b-np.dot(R,x))/D
  return x


# In[78]:


A = RandomMatrix
b = B
n = 25
x = np.ones((4, 4))

print(RandomMatrix)
print(B)
print(N)
print(x)


# In[79]:


jacobi(A, b, x, n)


# In[119]:


# 1 Norm
print(np.linalg.norm(B, ord=1))


# In[120]:


# Infinite form
infintie_norm_of_B = norm(B,inf)
print(infintie_norm_of_B)


# In[121]:


# Frobenius form
frobenius_norm_of_B = norm(B,'fro')
print(frobenius_norm_of_B)

