# Lab 4

from numpy import *
import sys

sys.stdout = open("output.txt", "w")

# Input data
Coeffs = [2, -1, -4, 2]
Ranges = [[-3,      -0.33333],
          [0.33333, 1       ],
          [1,       3       ]]
eps = 1e-6

def f(x):
    y = 0
    for i in range(0, len(Coeffs)):
        power = 1
        for j in range(0, i):
            power *= x
        y += Coeffs[i] * power
    return y

def df(x):
    y = 0
    for i in range(1, len(Coeffs)):
        power = i
        for j in range(1, i):
            power *= x
        y += Coeffs[i] * power
    return y

def bisec(a, b):
    print "Segment: [" + str(a) + ";" +  str(b) + "]"
    c = (1.0*a+b) / 2
    a1 = a
    b1 = b
    if (f(a) * f(c) > 0):
        a1 = c
        b1 = b
    else:
        a1 = a
        b1 = c
    if (abs(b1 - a1) < eps and abs(f((a1 + b1) / 2)) < eps):
        return c
    else:
        return bisec(a1, b1)

def chord(a, b, prev):
    print "Segment: [" + str(a) + ";" +  str(b) + "]"
    cur = (1.0*a*f(b) - b*f(a)) / (f(b) - f(a))
    a1 = a
    b1 = b
    if (f(a) * f(cur) > 0):
        a1 = cur
        b1 = b
    else:
        a1 = a
        b1 = cur
    if (abs(cur - prev) < eps and abs(f(cur)) < eps):
        return cur
    else:
        return chord(a1, b1, cur)

def newton(a, b, prev):
    print "Segment: [" + str(a) + ";" +  str(b) + "]"
    cur = 1.0*prev - 1.0*f(prev) / df(prev)
    a1 = a
    b1 = b
    if (f(a) * f(cur) > 0):
        a1 = cur
        b1 = b
    else:
        a1 = a
        b1 = cur
    if (abs(cur - prev) < eps and abs(f(cur)) < eps):
        return cur
    else:
        return newton(a1, b1, cur)

print "Bisec:"
for i in range(0, len(Ranges)):
    print "x" + str(i + 1) + ":"
    print "x" + str(i + 1) + "=" + str(bisec(Ranges[i][0], Ranges[i][1]))

print "Chord:"
for i in range(0, len(Ranges)):
    print "x" + str(i + 1) + ":"
    print "x" + str(i + 1) + "=" + str(chord(Ranges[i][0], Ranges[i][1], Ranges[i][1]))

print "Newton:"
for i in range(0, len(Ranges)):
    print "x" + str(i + 1) + ":"
    print "x" + str(i + 1) + "=" + str(newton(Ranges[i][0], Ranges[i][1], Ranges[i][1]))

sys.stdout.close()
sys.stdout = sys.__stdout__