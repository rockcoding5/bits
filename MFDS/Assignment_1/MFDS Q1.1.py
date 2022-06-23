# Assignment from Batch # 108 -

# Dheeraj Tuteja -
# Manikandana -
# Deepak -


# Q1.1 - Write a function to check whether a given square matrix is diagonally dominant. Test the function on a randomly
# generated 4 × 4 matrix.Deliverable(s) : Code that performs the check and the results obtained for the matrix 


import numpy as np

# Assumption for creating a matrix : Random log will choose integers between 2 an 12.
# Size of the Matrix is given in the problem statement 4 X 4
rand_matrx = np.random.randint(low=2, high=4, size=(4, 4))


# diagonally dominant - testing TRUE Scenario
# rand_matrx = [[3, -2, 1, 0],
#               [1, 5, 2, 1],
#               [-1, 2, 4, 0],
#               [2, -1, 3, 6]]

print(rand_matrx)
print(rand_matrx.shape)
print(rand_matrx.shape[0])


# Function to check diagonally dominant
def check_diagonal_dominant_matrix(matrix):
    num_rows = len(matrix)

    # Iterate all the rows of the matrix
    for row in range(0, num_rows):

        # Sum of all the columns elements in the given row.
        row_sum_value = 0
        for col in range(0, num_rows):
            row_sum_value = row_sum_value + abs(matrix[row][col])

        diagonal_row_value = abs(matrix[row][row])

        # Subtract the diagonal element from total value (row sum).
        row_sum_value = row_sum_value - diagonal_row_value

        # Check if diagonal element is less than sum of non-diagonal element.
        if diagonal_row_value < row_sum_value:
            return False

    return True


# Check given matrix is diagonal_dominant_matrix or not
if check_diagonal_dominant_matrix(matrix=rand_matrx):
    print("The matrix is a diagonally dominant matrix")
else:
    print("The matrix is not a diagonally dominant matrix")
