import random, sys, math
from typing import Union

def sign(x : Union[int, float]):
	# 1 if positive, 0 if 0, -1 if negative
	return (x > 0) - (x < 0)
	
def print_lines(n : int):
	# print a certain amount of empty lines
	print("\n" * n)
	return

def print_grid(grid : list, maxlen : int = 0):
	# cleanly prints a list of lists, spreadsheet-style. works best for a list of numbers
	if maxlen == 0:
		# look for longest item
		for itemx in grid:
			for itemy in itemx:
				if len(str(itemy)) > maxlen:
					maxlen = len(str(itemy))
	# maxlen of inner items
	maxlen2 = 0
	for itemx in grid:
		if len(itemx) > maxlen2:
			maxlen2 = len(itemx)
	# increase maxlen if it is lower than len(maxlen2)
	line = " " * (maxlen + 1)
	if maxlen < len(str(maxlen2)) + 1:
		maxlen = len(str(maxlen2)) + 1
	# y index
	for i in range(maxlen2):
		line += str(i+1) + ")"
		if maxlen > len(str(i+1)):
			line += " " * (maxlen - len(str(i+1)))
	print(line)
	# print items, now
	i = 1
	for itemx in grid:
		line = str(i) + ")"
		if maxlen > len(str(i)):
			line += " " * (maxlen - len(str(i)))
		for itemy in itemx:
			line += str(itemy) + " "
			if maxlen > len(str(itemy)):
				line += " " * (maxlen - len(str(itemy)))
		print(line)
		i += 1
		
def random_name(l : int = 2):
	# generates a random full name of length l (for example, if l=2, then it will generate a first and last name)
	NAMES = [
	"Jim", "Sal", "Sam", "Charles", "Lee", "Max", "Anita", "James", "Jane", "Cory", "Melony", "David", "Patricia", "Cal", "Jake", "Susie", "Lily", "Nia", "Margaret", "Marcel",
	"Alex", "Steve", "Johnson", "Jamal", "Peter", "Mason", "Cindy", "Louis", "Kelly", "Amanda", "Muhammad", "Carlos", "Lucita", "Milo", "Tucker", "Beatrice", "Julie",
	]
	name = ""
	for _ in range(l):
		name += random.choice(NAMES) + " "
	return name.strip()
