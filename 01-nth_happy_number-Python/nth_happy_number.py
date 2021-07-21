# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)
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

def nth_happy_number(n):
	found=0
	guess=0
	while(found<n):
		guess+=1
		if(ishappynumber(guess)):
			found+=1
	return guess

