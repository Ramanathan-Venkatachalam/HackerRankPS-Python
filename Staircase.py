#Staircase == Mirrored Right Triangle

def staircase(n):
    # Write your code here
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("#",end="")
        print()
        
"""
Simple Method == String Multiplication Method with Concatenation
 for i in range(n):
        print(" "*(n-i-1) + "#"*(i+1))
"""
