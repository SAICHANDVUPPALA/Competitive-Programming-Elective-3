# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def reverse(n):
	m=0
	while(n):
		r=n%10
		m=(m*10)+r
		n=n//10
	return m

def ispalindrome(n):
	
	return n==reverse(n)

def lychrelnumber(n):
	m=n
	if(n<10):
		return False
	for i in range(m):
		r=reverse(n)
		n=n+r
		if(ispalindrome(n)):
			return False
	return True

def nthlychrelnumbers(n):
	found=1
	guess=0
	while(found<=n):
		guess+=1
		if(lychrelnumber(guess)):
			found+=1
		
	return guess