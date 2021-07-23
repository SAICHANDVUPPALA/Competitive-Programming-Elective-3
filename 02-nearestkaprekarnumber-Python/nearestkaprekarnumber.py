# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



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



def fun_nearestkaprekarnumber(n):
    m=n
    p=n
    while(1):
        if(iskaprekarnumber(m)):
            k=m
            break
        else:
            m=m-1
    while(1):
        if(iskaprekarnumber(p)):
            l=p
            break
        else:
            p=p+1
    less=abs(n-k)

    great=abs(n-l)

    if(less<=great):
        return k
    elif(less>great):
        return l

