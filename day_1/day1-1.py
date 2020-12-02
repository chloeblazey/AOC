# --- Day 1: Report Repair ---
# ---       Part One       ---

# There are exactly two entries in day1.txt that sum to 2020.
# Multiply them and return their product.
# My solution has complexity O(n^2)

# reads nummbers line by line from a txt file
def main():
	# default filename is day1.txt
	FILENAME = "day1.txt"

	# convert filename to a list of ints called nums
	f = open(FILENAME)
	nums = []
	for n in f:
		nums.append(int(n))

	# brute force search for the two ints that add to 2020
	for n in nums:
		for m in nums:
			if n+m==2020:
				print(n*m) # multiply them and return their product
				return(n*m)

	# Give a no solution message if there's no sol'n
	print("no solution")
	return 0

if __name__ == '__main__':
	main()