# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	if(n>0):
		if(n>len(s)):
			n=n-len(s)
		tmp = s[n:] + s[0:n]
		return tmp
	elif(n<0):
		n=-n
		d=len(s)-n
		tmp=s[d:]+s[0:d]
		return tmp
	else:
		return s
	

