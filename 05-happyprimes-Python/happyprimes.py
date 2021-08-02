# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def digits_sum(n):
	sum=0
	while(1):
		r=n%10
		sum+=r*r
		n=n//10
		
		if(n==0):
			if(sum>=10):
				n=sum
				sum=0
			else:
				return sum
def ishappynumber(n):
	#your code goes here
	if(n==1):
		return True
	
	elif(n<1):
		return False
	sum=digits_sum(n)
	if(sum==1):
		return True
	else:
		return False

def isprime(n):
    if(n==2):
        return True
    elif(n>2):
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                return False
    return True

def ishappyprimenumber(n):
    # Your code goes here
    if(ishappynumber(n) and isprime(n)):
        return True
    else:
        return False
           
        