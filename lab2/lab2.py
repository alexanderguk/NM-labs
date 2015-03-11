# Gauss–Seidel method

from numpy import *
import sys

sys.stdout = open("output.txt", "w")

# Input data
A = matrix([[3.81, 0.25, 1.28, 0.75],
            [2.25, 1.32, 4.58, 0.49],
            [5.31, 6.28, 0.98, 1.04],
            [9.39, 2.45, 3.35, 2.28]])
B = matrix([[ 4.21],
            [ 6.47],
            [ 2.38],
            [10.48]])
eps = 1e-6

Borig = B.copy()
Aorig = A.copy()

print "---Input matrix A---"
print A
# Preprocessing: Creating of Diagonally dominant matrix
A[[0, 3],:] = A[[3, 0],:]
B[[0, 3],:] = B[[3, 0],:]
print "--------"
print A
A[:,[1, 2]] = A[:,[2, 1]]
print "--------"
print A
A[2] -= 0.7*A[0]
B[2] -= 0.7*B[0]
print "--------"
print A
A[3] -= 0.4*A[0]
B[3] -= 0.4*B[0]
print "--------"
print A
A[3] += 0.15*A[2]
B[3] += 0.15*B[2]
print "--------"
print A
A[3] += 0.05*A[1]
B[3] += 0.05*B[1]
print "---Diagonally dominant matrix A---"
print A
print "---Input matrix B---"
print B

# Gauss–Seidel method
n = A.shape[0]
x = zeros((n, 1))  
conv = False
it = 0
while not conv:
    p = x.copy()
    for i in range(n):
        var = 0
        for j in range(i):
            var += A[i, j] * x[j]
        for j in range(i + 1, n):
            var += A[i, j] * p[j]
        x[i] = (B[i] - var) / A[i, i]
    
    conv = True
    for i in range(n):
        if abs(x[i] - p[i]) > eps:
            conv = False
    
    # Output for each iteration
    r = Borig - Aorig * x # residual vector
    it += 1
    print "---Iteration " + str(it) + ": Residual vector---\n" + str(r)
    print "---Iteration " + str(it) + ": X---\n" + str(x)

sys.stdout.close()
sys.stdout = sys.__stdout__