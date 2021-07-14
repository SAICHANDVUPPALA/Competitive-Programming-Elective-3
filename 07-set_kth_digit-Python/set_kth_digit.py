# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 






def fun_set_kth_digit(n, k, d):
	neg=False
	if(n<0):
		n=-n
		neg=True
	result=0
	count=0
	while(n>0):
		rem=n%10
		if(count==k):
			result=result+(d*(10**count))
		else:
			result=result+(rem*(10**count))
		count+=1
		n=n//10
	if(count==k):
		result=result+(d*(10**count))
	if(neg):
		return -result
	else:
		return result


