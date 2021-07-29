# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

def alternatingsum(l,n,sum):
	if(n==len(l)):
		return sum
	elif(n%2==0):
		sum+=l[n]
		return alternatingsum(l,n+1,sum)
	else:
		sum-=l[n]
		return alternatingsum(l,n+1,sum)
def fun_recursions_alternatingsum(l):
	if(len(l)==0):
		return 0
	sum=l[0]
	result=alternatingsum(l,1,sum) 
	return result
