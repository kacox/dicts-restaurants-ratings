"""Restaurant rating lister.

Tasks:
	Reads the ratings in from the file
	Stores them in a dictionary
	And finally, spits out the ratings in alphabetical order by restaurant.

Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.

Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.
"""

import sys

def read_ratings(filename):
	""" """
	# init empty dict
	restaurant_ratings = {}

	# build dictionary using text file
	with open(filename, 'r') as file:
		for line in file:
			cleaned_line = line.rstrip()
			resturant_and_rating = cleaned_line.split(":")
			restaurant_ratings[resturant_and_rating[0]] = int(resturant_and_rating[1])

	return restaurant_ratings


def sort_ratings(dictionary):
	""" """
	pass


def print_ratings():
	""" """
	pass


read_ratings(sys.argv[1])