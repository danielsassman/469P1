
# given an integer n, and optionally a dictionary results (whose keys are ints k and whose values are the result of fast_fib(k)),
# calculate the nth fibonnaci number while memoizing the answers (don't use the pathologically slow recursive approach). 
def fast_fib(n, results={}):
	if n in results:
		return results[n]
	elif n==0:
		return 0
	elif n== 1:
		return 1
	else:
		results[n] = fast_fib(n-1) + fast_fib(n-2)
		return results[n]

# given a list of values, create a new list with the same values in reversed order. Do not modify the original list. 
def reversed(xs):
	listLength = len(xs)-1
	newList = []
	while(listLength>=0):
		newList.append(xs[listLength])
		listLength = listLength - 1 
	return newList


# check if the argument n is prime (is only divisible by 1 and itself). The smallest prime is 2. 
def is_prime(n):
	if(n<2): 
		return False
	for i in range(2,n-1):
		if(n%i==0):
			return False
	return True


# return a list of all values that show up in xs at least once. The answer must not include any duplicates, and must report the occurring values in the same order as their first occurrence. 
def nub(xs):
	if(len(xs)<=1):
		return xs
	newList = []
	for x in xs:
		if x not in newList:
			newList.append(x)
	return newList


# given a two-argument function and two lists of arguments to supply, create a list of the results of applying the function to each 
# same-indexed pair of arguments from the two lists. (Zip up the two lists with the function). 
def zip_with(f, xs, ys):
	newList = []
	if(len(xs) <= len(ys)):
		for x in range(0, len(xs)):
			newList.append(f(xs[x],ys[x]))
	else:
		for x in range(0, len(ys)):
			newList.append(f(xs[x],ys[x]))
	return newList


# given a number n, we generate successive integer values in a sequence, which must end with a 1. The rules for successive values are:
#        if n is 1, the sequence ends.
#        if n is even, the next number is n/2.
#        if n is odd, the next number is n*3+1.
def collatz(n):
	newList = [n]
	while n != 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = n * 3 + 1 	
		newList.append(n)
	return newList


# Given the name of a text file that contains one or more lines, each with a single integer on that line, calculate these three properties and return in a triplet: (mean, median, mode)
#        mean is the average.
#        median is the middle value of the sorted values; in case of even length, average them.
#        the mode must be a list of all values that share the most occurrences, ordered increasing. This list might only have one value in it.
def file_report(filename):
	newList = []
	intList = []
	with open(filename) as f:
		lines = [line.rstrip('\n') for line in open(filename)]
		newList.append(lines)
	newList = newList[0]
	for x in newList:
		intList.append(int(x))
	intList.sort()
	return (mean(intList), median(intList), mode(intList))

def median(xs):
	if len(xs) <=1:
		return xs
	mid = int(len(xs)/2)
	if len(xs) % 2 == 0:
		retVal = ((xs[mid-1]+xs[mid])/2)
		if retVal % 1 == 0:
			return int(retVal)
		else:
			return retVal
	return (int(xs[mid]))

def mean(xs):
	avg = 0
	for x in range(len(xs)):
		avg = avg + xs[x]	
	return avg/len(xs);
	
def mode(xs):
	modeList = []
	count = 0
	holder = xs[0]-1
	maxCount = 0
	for x in range(len(xs)):
		if xs[x] == holder:
			if maxCount == 0:
				modeList[:] = []
				maxCount = 1
			count = count + 1
			if count == maxCount or maxCount==0:
				if xs[x] not in modeList:
					modeList.append(xs[x])
			if count > maxCount:
				maxCount = maxCount + 1
				modeList[:] = []
				modeList.append(xs[x])	 
		elif maxCount == 0:
			modeList.append(xs[x])
			holder = xs[x]
		else:
			holder = xs[x]
			count = 0
	return modeList


# Given a 9x9 2d list, check if it represents a valid, solved sudoku. 
def check_sudoku(grid):
	return check_rows(grid) and check_cols(grid) and check_squares(grid)

def check_cols(grid):
	newGrid = []
	check = 9
	colCount = -1
	cleanList = []
	for z in range(0,9):
		for p in range(0,9):
			cleanList.append((grid[p][z]))
			if len(cleanList) % 9 == 0:
				newSet = set(cleanList)
				cleanList = []
				if len(newSet) != 9:
					return False
	return True

def check_rows(grid):
	for x in grid:
		if len(x) != 9:
			return False
		newSet = set(x)
		if len(newSet) != 9:
			return False		
	return True

def check_squares(grid):
	list1 = []
	list2 = []
	list3 = []
	
	cleanList = []
	for z in range(0,9):
		for p in range(0,9):
			cleanList.append(grid[p][z])
	for n in range(0,81):
		if n % 9 == 0 or  n%9 ==1  or n%9 ==2:
			list1.append(cleanList[n])
		elif n%9 ==3 or n%9==4 or n%9 ==5:
			list2.append(cleanList[n])
		else:
			list3.append(cleanList[n])
		if n== 26 or n == 53 or n ==80:
			set1 = set(list1)
			set2 = set(list2)
			set3 = set(list3)
			setLength = len(set1) + len(set2) + len(set3)
			if setLength != 27:
				return False
			list1 = []
			list2 = []
			list3 = []
	return True		

