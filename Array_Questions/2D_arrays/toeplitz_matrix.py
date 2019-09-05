
#bounds of our matrix, 5X4 
N = 5
M = 4

# Function to check if all elements present in 
# descending diagonal starting from position 
# (i, j) in the matrix are all same or not 
def checkDiagonal(mat, i, j): 
	res = mat[i][j]
	i += 1
	j += 1
	
	while (i < N and j < M): 
		
		# mismatch found 
		if (mat[i][j] != res): 
			return False
			
		i += 1
		j += 1

	# we only reach here when all elements 
	# in given diagonal are same 
	return True

# Function to check whether given 
# matrix is a Toeplitz matrix or not 
def isToeplitz(mat): 
	
	# do for each element in first row 
	for j in range(M): 
		
		# check descending diagonal starting from 
		# position (0, j) in the matrix 
		if not(checkDiagonal(mat, 0, j)): 
			return False
	
	# do for each element in first column 
	for i in range(1, N): 
		
		# check descending diagonal starting 
		# from position (i, 0) in the matrix 
		if not(checkDiagonal(mat, i, 0)): 
			return False
		
	return True

# Driver Code 
if __name__ == "__main__": 
		
	mat = [[6, 7, 8, 9], 
		[4, 6, 7, 8], 
		[1, 4, 6, 7], 
		[0, 1, 4, 6], 
		[2, 0, 1, 4]] 

	if(isToeplitz(mat)): 
		print("Matrix is a Toeplitz") 
	else: 
		print("Matrix is not a Toeplitz") 

