# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def powerSum(n, k):
    # Your code goes here...
    if(n<0 or k<0):
        return 0
    sum=0
    for i in range(1,n+1):
        sum+=i**k

    return sum

def repowerSum(n,k):
    if(k<0 or n<0):
        return 0
    sum=n**k
    return sum+repowerSum(n-1,k)

# Write your own test cases here...
assert(repowerSum(1,3)==1)
assert(repowerSum(5,2)==55)
print ("All test cases passed...")