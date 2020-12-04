# --- Day 3: Toboggan Trajectory ---
FILENAME = 'day3.txt'
with open(FILENAME) as f:
	map = f.read().split()

treeCount = 0
sledPosition = 0

for row in map:
	i = sledPosition % len(row)
	if row[i] == '#':
		treeCount += 1
		print(row[0:i]+'X'+row[i+1:len(row)])
	else:
		print(row[0:i]+'O'+row[i+1:len(row)])
	sledPosition += 3

print(treeCount)

