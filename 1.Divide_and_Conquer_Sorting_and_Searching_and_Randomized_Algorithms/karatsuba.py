'''
In this programming assignment you will implement one or more of the integer 
multiplication algorithms described in lecture.

To get the most out of this assignment, your program should restrict itself to 
multiplying only pairs of single-digit numbers.  You can implement the grade-school 
algorithm if you want, but to get the most out of the assignment you'll want to 
implement recursive integer multiplication and/or Karatsuba's algorithm.
'''
from math import ceil

def length(x:int) -> int:
    return len(str(x))

def karatsuba(x:int, y:int) -> int:
    lx = length(x)
    ly = length(y)
    
    if lx==1 or ly==1:
        return x*y
    else:
        N = max(lx, ly)
        m = ceil(N/2)
        zeros = 10**m
        
        a = x // zeros
        b = x % zeros
        c = y // zeros
        d = y % zeros
        
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ab_cd = karatsuba(a+b, c+d) - ac - bd
        
        return ac*zeros*zeros + ab_cd*zeros + bd
    
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(x, y))