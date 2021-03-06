# --- Day 2: Password Philosophy ---
# -----        Part 1        -------
# given a rule and a password, returns true if pw is valid
def processRule(rule):
	position1 = int(rule.split('-')[0])
	position2 = int(rule.split('-')[1])
	return (position1, position2)

def processChar(c):
	return c[0]

def isValid((rule, c, pw)):
	(lo, hi) = processRule(rule)
	c = processChar(c)
	count = 0;
	# count how many times ch appears in pw.
	for char in pw:
		if char == c:
			count = count + 1
	# if count is between the rule boundaries, return true.
	if lo <= count <= hi: 
		return True
	else: 
		return False

def main():
	FILENAME = 'day2.txt'
	f = open(FILENAME)
	# Store each password as an array of strings:
	# [['1-3', 'a:', 'abcde'], ['1-3', 'b:', 'cdefg'], ['2-9', 'c:', 'ccccccccc']]
	passwords = list(map( lambda line: tuple(line.split()) , f ))
	count = len( list( filter( isValid, passwords )))
	print count

if __name__ == '__main__':
	main()