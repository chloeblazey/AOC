# --- Day 1: Report Repair ---
# ---       Part Two       ---
# Find 3 numbers in the file day1.txt that sum to 2020.
# Return their product.
def main():
	FILENAME = "day1.txt"

	f = open( FILENAME )
	nums = []
	for n in f:
		nums.append( int(n) )

	# cycle thru every possible pair of numbers...
	for i in range( len(nums) ):
		x = nums[ i ]
		if x < 2020:
			for j in range( i+1 , len(nums) ):
				y = nums[ j ]
				if x + y < 2020:
					# once you find a pair that adds to less than 2020,
					# cycle thru every trio of numbers which includes this pair.
					for k in range( j+1 , len(nums) ):
						z = nums[ k ]
						# if the trio adds to 2020, you've got your man.
						if x + y + z == 2020:
							print( x * y * z )
							return x * y * z
	print( 'No solution' )
	return 0

if __name__ == '__main__':
	main()