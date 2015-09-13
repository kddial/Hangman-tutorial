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

	# Loop through the game
	while winner == False and hangman_lives > 0:
		output_hangman_stats() # Output hangman stats
		user_input = get_user_input() # User inputs letter

		# If the letter is correct, display correct message
		# else, add a body part to the hangman
		if user_input in hangman_word:
			# append to correct letters
			correct_letters.append(user_input)

			# Check for winner
			for letter in hangman_word:
				if letter not in correct_letters:
					winner = False
					break
				else:
					winner = True
		else:
			# reduce lives by 1
			hangman_lives = hangman_lives - 1
			# append fail letters
			fail_letters.append(user_input)

	output_hangman_stats()
	if winner:
		print("You win!")
		print("The word:", hangman_word)
	else:
		print("Game overrrrrrrrrr, no more lives")

