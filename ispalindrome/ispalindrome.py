
def ispalindrome(n):
    p=0
    m=n
    while(n):
        r=n%10
        n=n//10
        if(n==0):
            p+=r
        else:
            p+=r
            p=p*10
    if(p==m):
        
        return True
    return False

def isprime(n):
    if(n==2):
        return True
    elif(n<2):
        return False
    elif(n>2):
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                return False
    return True

def isPalindromicPrime(n):
    if(ispalindrome(n) and isprime(n)):
        return True
    return False


assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")