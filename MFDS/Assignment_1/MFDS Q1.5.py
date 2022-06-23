#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Assignment from Batch # 287 - 

#Dheeraj Tuteja -
#Manikandana - 
#Deepak -


# In[30]:


# Q1.5 - Write a function that perform  Gauss Jacobi iterations. Generate a random 4 × 4 matrix A and generate a random b ∈ R^4
# Report the results of passing this matrix to function written in (i). Solve linear system Ax = b by using function in (ii). 
# Generate a plot of ∥xk+1 − xk∥2 for first 100 iterations. Does it converge ? or Is it diverging? Specify your observation. 
# Take a screenshot of plot and paste it in the assignment document.

# Repeat part (iv) for the Gauss Jacobi iteration


# In[31]:


#import numpy
import numpy as np
from numpy import array,inf
from numpy.linalg import norm 
from scipy.linalg import solve

np.seterr(divide='ignore', invalid='ignore')


# In[33]:


# Generate Random Matrix

RandomMatrix = np.random.randint(100, size=(4, 4)) 
# Assumption for creating a matrix : Random log will choose integers between 1 an 10.
# Size of the Matrix is given in the problem statement 4 X 4 

print((RandomMatrix)) #Print Array (matrix)
print(type(RandomMatrix)) #Print type of the array
print(RandomMatrix.shape) #Print shape of the array

B = np.random.randint(100, size=(4, 1)) # AX = B (RHS)
print((B)) #Print Array (matrix)
print(type(B)) #Print type of the array
print(B.shape) #Print shape of the array


# In[34]:


# Funnction to check diagonally dominant
def IsDiagonallyDominant(MyMatrix):
    D = np.diag(np.abs(MyMatrix)) # Find diagonal coefficients
    S = np.sum(np.abs(MyMatrix), axis=1) - D # Find row sum without diagonal
    if np.all(D > S):
        print ('matrix is diagonally dominant')
    else:
        print ('NOT diagonally dominant')
    return


# In[35]:


#Call the function and pass the numpy array (matrix)
IsDiagonallyDominant(RandomMatrix)


# In[36]:


from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A,b,N=99,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
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
        x = (b - dot(R,x)) / D
    return x


# In[37]:


# int(input())input as number of variable to be solved
A = RandomMatrix
b = B
N = 99
# initial solution depending on n(here n=3)
x = np.ones((4, 1), dtype = int)

print(A)
print(b)
print(N)
print(x)


# In[38]:


sol = jacobi(A,b,N,x)

print ("A:")
pprint(A)

print ("b:")
pprint(b)

print ("x:")
pprint(sol)


# In[28]:


import matplotlib.pyplot as plt

plt.plot(x)
#plt.yscale('log')
plt.show()


# In[ ]:




