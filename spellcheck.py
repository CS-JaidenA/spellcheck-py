# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time
from math import floor

def linear_search(list, item):
    for i, v in enumerate(list):
        if v == item:
            return i
    return -1

def binary_search(list, item):
	lower = 0
	upper = len(list) - 1

	while upper >= lower:
		middle = floor((lower + upper) / 2)
		middle_item = list[middle]

		if item == middle_item:
			return middle
		elif item < middle_item:
			upper = middle - 1
		else: # item > middle_item
			lower = middle + 1
	
	return -1

def search(list, dictionary, algorithm):
	length = len(list)
	not_found_count = 0
	print(f"{'Linear' if algorithm == linear_search else 'Binary'} search starting...")

	start_time = time.time()

	for i, word in enumerate(list):
		if algorithm(dictionary, word.lower()) == -1:
			not_found_count += 1
		print(f"{i}/{length}", end='\r')
	
	end_time = time.time()

	print(f"Number of words not found in dictionary: {not_found_count} ({end_time - start_time}) s")

def spellcheck(list, word, algorithm):
	print(f"{'Linear' if algorithm == linear_search else 'Binary'} search starting...")

	start_time = time.time()
	index = algorithm(list, word)
	end_time = time.time()

	elapsed_time = (end_time - start_time) * 1000

	if index > -1:
		print(f"{word} is IN the dictionary at position {index}. ({elapsed_time}) ms")
	else:
		print(f"{word} is NOT IN the dictionary. ({elapsed_time}) ms")

def main():
	# Load data files into lists
	dictionary = loadWordsFromFile("data-files/dictionary.txt")
	aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

	# Print first 50 values of each list to verify contents
	print(dictionary[0:50])
	print(aliceWords[0:50])

	print()

	while True:
		print("Main Menu")
		print("1: Spell Check a Word (Linear Search)")
		print("2: Spell Check a Word (Binary Search)")
		print("3: Spell Check Alice In Wonderland (Linear Search)")
		print("4: Spell Check Alice In Wonderland (Binary Search)")
		print("5: Exit")

		print()

		selection = input("Enter menu selection (1-5): ")

		print()

		match selection:
			case "1":
				word = input("Please enter a word: ").lower()
				spellcheck(dictionary, word, linear_search)
			case "2":
				word = input("Please enter a word: ").lower()
				spellcheck(dictionary, word, binary_search)
			case "3":
				search(aliceWords, dictionary, linear_search)
			case "4":
				search(aliceWords, dictionary, binary_search)
			case "5":
				break
			case _:
				print("Invalid input! Please try again...")

		print()

def loadWordsFromFile(fileName):
	# Read file as a string
	fileref = open(fileName, "r")
	textData = fileref.read()
	fileref.close()

	# Split text by one or more whitespace characters
	return re.split('\s+', textData)

main()
