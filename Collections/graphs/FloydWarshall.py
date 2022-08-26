# Floyd Warshall:

# All pair shortest path:


# Pre-Requisite:
# No negative Cycle


# 1. consider an adjecency matrix A, given to you for a weighted directed graph.
# n = number of vertices so A is of size nxn (nodes : 1 to n )

# initially, A[i][j] = weight of the edge from i to j, infinity if edge doesn't exist, 0 if i is same as j


# 2. Now we create an A1 matrix by relaxing all values through node 1. 

# So node 1 and edges directly from node 1 will not change.
# => 1st row and col will not change

# For others paths i to j

# A1[i,j] = min(A[i,j], A[i,1]+A[1,j])


# 3. Do this n times, for all nodes

# for k (1 to n):
# 	for i (1 to n):
# 		for j (1 to n):
# 			A[i][j] = min(A[i,j],A[i][k]+A[k][j])



# TC : n^3