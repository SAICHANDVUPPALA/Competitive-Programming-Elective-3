# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def iskaprekarnumber(n):
    if(n==0):
        return False
    elif(n==1):
        return True
    
    if(n**2<10):
        return False
    m=str(n**2)
    l=len(m)
    m1=m[0:int(l/2)]
    m2=m[int(l/2):l]
    
    sum=int(m1)+int(m2)
    
    if(sum==n):
        return True
    else:
        while(len(m1)):
            if(m1[-1]=='0'):
                m1=m1[0:-1]
            else:
                break
        while(len(m2)):
            if(m2[-1]=='0'):
                m2=m2[0:-1]
            else:
                break
        if(len(m1)==0 or len(m2)==0):
            return False
        sum=int(m1)+int(m2)
        if(sum==n):
            return True
    return False



def fun_nth_kaprekarnumber(n):
    found=0
    guess=0
    while(found<=n):
        guess+=1
        if(iskaprekarnumber(guess)):
            found+=1
    return guess

