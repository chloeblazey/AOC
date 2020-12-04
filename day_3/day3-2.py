# --- Part Two ---
import sys

def countTrees(field, over, down):
	field = field[::down]
	treeCount = 0
	sledPosition = 0

	for row in field:
		i = sledPosition % len(row)
		if row[i] == '#':
			treeCount += 1
			print(row[0:i]+'X'+row[i+1:len(row)])
		else:
			print(row[0:i]+'O'+row[i+1:len(row)])
		sledPosition += over

	return(treeCount)

def main(argv):
	FILENAME = argv[1]
	slopes = map(lambda x: tuple(x), argv[2:])

	with open(FILENAME) as f:
		field = f.read().split()

	prod = 1
	for over, down in slopes:
		prod *= countTrees(field, int(over), int(down))
	print prod
	return prod

if __name__ == '__main__':
	main(sys.argv)