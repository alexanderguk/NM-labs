# Lab 3

from numpy import *
import sys

sys.stdout = open("output.txt", "w")

# Input data
A = matrix([[ 6.81,   1.12,   0.95,   1.165],
            [ 1.12,   3.61,   1.3,    0.16 ],
            [ 0.95,   1.3,    5.99,   2.1  ],
            [ 1.165,  0.16,   2.1,    5.55 ]])
Aorig = A.copy()

# Danilevskiy method
m = A.shape[0]
Aprev = A.copy()
k = 0
p = full(m, 'nan')
for i in range(1, m):
    Aprev = A.copy()
    
    skipStep = False
    if Aprev[m-i, m-i-1] == 0:
        l = -1
        for j in range(m-i):
            if (Aprev[m-i, j]) != 0:
                l = j
                break
        if l >= 0:
            Aprev[[m-i-1, l],:] = Aprev[[l, m-i-1],:]
            Aprev[:,[m-i-1, l]] = Aprev[:,[l, m-i-1]]
        else:
            k = i
            skipStep = True
            for e in range(m-k, m):
                if not isnan(p[e]):
                    break
                p[e] = Aprev[m-k, e]
            
    if not skipStep:
        M = eye(m, m)
        for j in range(m-k):
            if j != m - i - 1:
                M[m-i-1, j] = -Aprev[m-i, j] / Aprev[m-i, m-i-1]
            else:
                M[m-i-1, j] = 1 / Aprev[m-i, m-i-1]
        Minv = eye(m, m)
        for j in range(m-k):
            Minv[m-i-1, j] = Aprev[m-i, j]
        
        print "---Step: " + str(i) + ". Matrices M and M-1---"
        print M
        print Minv
        A = Minv*Aprev*M

for e in range(0, m):
    if not isnan(p[e]):
        break
    p[e] = A[0, e]

set_printoptions(precision=5)
set_printoptions(suppress=True)
print "---Result---"
print A
print "---p elemets---"
print p

sys.stdout.close()
sys.stdout = sys.__stdout__