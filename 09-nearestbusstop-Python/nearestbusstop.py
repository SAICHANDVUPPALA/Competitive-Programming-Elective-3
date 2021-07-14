# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	if(street==0):
		return 0
	for i in range(0,street,8):
		if(i==0):
			if(street<=8 and street>4):
				return 8
			elif(street<=4):
				return 0
		else:
			if(street>=i and street<=2*i-4):
				return i
			else:
				return 2*i
