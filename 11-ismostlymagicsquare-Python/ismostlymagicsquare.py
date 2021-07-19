# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
	if(len(a)==1 and len(a[0])==1):
		return True
	else:
		#row
		sumofrow=[]
		for i in range(len(a)):
			sum=0
			for j in range(len(a[0])):
				sum+=a[i][j]
			sumofrow.append(sum)
		rows=sumofrow.count(sumofrow[0])==len(sumofrow)
		# print(rows)
		if(rows):
			#column
			sumofcol=[]
			for i in range(len(a[0])):
				sum=0
				for j in range(len(a)):
					sum+=a[i][j]
				sumofcol.append(sum)
			# print(sumofrow,sumofcol)
			cols=sumofcol.count(sumofcol[0])==len(sumofcol)
			if(cols):
				#diagonal
				d1=0
				d2=0
				for i in range(len(a)):
					d1+=a[i][i]
					d2+=a[i][-1-i]
				if(d1==d2):
					return True
	return False

