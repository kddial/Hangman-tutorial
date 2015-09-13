# Hangman game

####### Import libraries ########
import random



####### Functions ########

# Output lives, body, correct and fail letters, hangman word
def output_hangman_stats():
	print("----------------------------------")
	# Output of lives
	output_lives = ["Number of lives: ", hangman_lives]

	# Output body
	if hangman_lives == 6:
		output_body = [" ", " ", " ", " ", " "]
	if hangman_lives == 5:
		output_body = ["  O  ", " ", " ", " ", " "]
	if hangman_lives == 4:
		output_body = ["  O  ", "  |  ", " ", " ", " "]
	if hangman_lives == 3:
		output_body = ["  O  ", "/ |  ", " ", " ", " "]
	if hangman_lives == 2:
		output_body = ["  O  ", "/ | \\", " ", " ", " "]
	if hangman_lives == 1:
		output_body = ["  O  ", "/ | \\", " /", " ", " "]
	if hangman_lives == 0:
		output_body = ["  O  ", "/ | \\", "  /\\", " ", " "]

	# Output correct and fail letters
	output_letters = []
	output_letters.append("\nCorrect letters: ")
	for letter in correct_letters:
		output_letters.append(letter)
		output_letters.append(", ")
	output_letters.pop()

	output_letters.append("\nFail letters: ")
	for letter in fail_letters:
		output_letters.append(letter)
		output_letters.append(", ")
	output_letters.pop()

	# Output hangman word
	output_word = []
	for letter in hangman_word:
		if letter in correct_letters:
			output_word.append(letter)
		else:
			output_word.append("_")

	print(*output_lives, sep="")
	print(*output_body, sep="\n")
	print(*output_letters, sep="")
	print(*output_word, sep=" ")
	print()

# Ask user for a letter
# Only 1 letter, make sure it wasnt entered before, non-empty
def get_user_input():
	while True:
		user_input = input("Please type a letter: ")
		if len(user_input) == 1:
			if user_input not in correct_letters and user_input not in fail_letters:
				return user_input
			else:
				print("Letter already entered, try another letter\n")
		else:
			print("Please enter only 1 letter\n")

# Clear out some noise from main
def init_logic():
	print("\n\n\n\n\n")
	print("Welcome to Hangman!\n")

	# Choose the hangman word by random
	random.seed()



####### Initialize variables #######

# Keep a list of words to play with
words = ["apple", "cucumber", "tomato", "kale", "kombucha", "mango", "watermelon", "guava", "avocado"]

# Keep a list of correct user letters
correct_letters = []

# Keep a list of fail user letters
fail_letters = []

# Keep track of hangman lives
hangman_lives = 6 # do not change

# Keep track of winner
winner = False



####### Logic for the game #######
if __name__ == '__main__':

	init_logic() # initialize logic
	hangman_word = random.choice(words) # choose random word


	output_hangman_stats() # Output hangman stats
	user_input = get_user_input() # User inputs letter

	### TODO 1: implement the logic to check if the user input is inside the hangman word ###

	### TODO 2: loop until lives run out or until there is a winner ###

	### TODO 3: output if the user is a winner or a loser ###





















