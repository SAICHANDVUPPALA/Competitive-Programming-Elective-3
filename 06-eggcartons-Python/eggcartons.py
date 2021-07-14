# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs

import math
def fun_eggcartons(eggs):
	# your code goes here
	count=0
	if(eggs==0):
		return 0
	if(eggs<=12):
		return 1
	carton=math.ceil(eggs/12)
	return carton
