# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	# your code goes here
	a1,b1,c1=m1,-1,b1
	a2,b2,c2=m2,-1,b2
	n=(b1*c2) - (b2*c1)
	d=(a1*b2) - (a2*b1)

	if(m1==m2):
		return None
	elif(n/d<=1):
		return None
	else:
		return n/d

	

