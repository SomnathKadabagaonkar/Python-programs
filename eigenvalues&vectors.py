import numpy as np

A= np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
values,vector = np.linalg.eig(A)
print("eigenvalue")
print(values)
print("Eigenvector")
print(vector)

P=vector

D=np.diag(values)
P_inv=np.linalg.inv(P)

print("Diagonal")
print(D)

print("Matrix P")
print(P)

print("inverse of p ")
print(P_inv)

print("Diagonalisation")
print(D @ P @ P_inv)
