# -*- coding: utf-8 -*-

from numpy import *

# Variant
# Nvar = 5
# k = Nvar - 5 = 0
# a = 0.2k = 0
# b = 0.2k = 0

# Input data

A = matrix([[8.30, 2.62, 4.10, 1.90],
            [3.92, 8.45, 8.87, 2.46],
            [3.77, 7.21, 8.04, 2.28],
            [2.21, 3.65, 1.69, 6.99]])

B = matrix([[-10.65],
            [ 12.21],
            [ 15.45],
            [- 8.35]])

Borig = B.copy()
Aorig = A.copy()

n = A.shape[0]

# Part 1
ATemp = zeros((n, n))
BTemp = zeros((n, 1))
    
p = full(n, -1)
q = full(n, -1)
    
print A    
    
for curN in range(n, 0, -1):
    # Looking for main element a(main)
    aMain = -float('inf')
    for i in range(n):
        if not i in p:
            for j in range(n):
                if not j in q:
                    if A[i, j] > aMain:
                        aMain = A[i, j]
                        p[curN - 1] = i
                        q[curN - 1] = j
    
    # Calculation m(i)
    m = zeros(n)
    for i in range(n): 
        m[i] = (A[i, q[curN - 1]] / A[p[curN - 1], q[curN - 1]])
            
    # Substracting all rows except p
    for i in range(n):
        if not i in p:
            for j in range(n):
                if not j in q or j == q[curN - 1]:
                    A[i, j] -= m[i] * A[p[curN - 1], j]
            B[i] -= m[i] * B[p[curN - 1]]

    for i in range(n):
        for j in range(n):
            if abs(A[i, j]) < 1e-6:
                A[i, j] = 0

    #print A    
    
print A    
print B
print "---"        

# Part 2
for curN in range(n):
    # Calculation m(i)
    m = zeros(n)
    for i in range(n): 
        m[i] = (A[i, q[curN]] / A[p[curN], q[curN]])
            
    # Substracting all rows except p
    for i in range(n):
        if i != p[curN]:
            for j in range(n):
                A[i, j] -= m[i] * A[p[curN], j]
            B[i] -= m[i] * B[p[curN]]

    for i in range(n):
        for j in range(n):
            if abs(A[i, j]) < 1e-6:
                A[i, j] = 0
    
print A
            
x = zeros((n, 1))            
for i in range(n):
    print "x" + str(q[i]) + "=" + str(B[p[i]] / A[p[i], q[i]])
    x[q[i]] = B[p[i]] / A[p[i], q[i]]

# Vector r calculation

r = Borig - Aorig * x

print r
