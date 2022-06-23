#!/usr/bin/env python
# coding: utf-8

# In[80]:


# Assignment from Batch # 287 - 

#Dheeraj Tuteja -
#Manikandana - 
#Deepak -


# In[81]:


# Q1.4 - Write a function that perform Gauss Seidel iterations. Generate a random 4 × 4 matrix A and generate a random b ∈ R^4
# Report the results of passing this matrix to function written in (i). Solve linear system Ax = b by using function in (ii). 
# Generate a plot of ∥xk+1 − xk∥2 for first 100 iterations. Does it converge ? or Is it diverging? Specify your observation. 
# Take a screenshot of plot and paste it in the assignment document.


# In[82]:


#import numpy
import numpy as np
from numpy import array,inf
from numpy.linalg import norm 
from scipy.linalg import solve


# In[83]:


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


# In[84]:


# Funnction to check diagonally dominant
def IsDiagonallyDominant(MyMatrix):
    D = np.diag(np.abs(MyMatrix)) # Find diagonal coefficients
    S = np.sum(np.abs(MyMatrix), axis=1) - D # Find row sum without diagonal
    if np.all(D > S):
        print ('matrix is diagonally dominant')
    else:
        print ('NOT diagonally dominant')
    return


# In[85]:


#Call the function and pass the numpy array (matrix)
IsDiagonallyDominant(RandomMatrix)


# In[86]:


# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix

def gauss_seidel(a, x ,b):
    #Finding length of a(3)	
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if(j != i):
                d = d.astype('float64')
                d-=a[j][i] * x[i]
                
        # updating the value of our solution
        x[j] = d / a[j][j]
    # returning our updated solution
    return x



# In[87]:


# int(input())input as number of variable to be solved
n = 100 # As mention in problem statement
a = RandomMatrix
b = B
# initial solution depending on n(here n=3)
x = np.ones((4, 1), dtype = int)

print(n)
print(a)
print(b)
print(x)


# In[88]:


#loop run for m times depending on m the error value
for i in range(0, n-1):
    x = gauss_seidel((a), (x), (b))
    #print each time the updated solution
    print(x)


# In[90]:


import matplotlib.pyplot as plt

plt.plot(x)
#plt.yscale('log')
plt.show()


# In[ ]:




