###### The Guessing Game ########
#MY CODE:
import random
from art import logo
EASY_LIVES = 10
HARD_LIVES = 5
#Display the LOGO

#Guess the a random number
def random_number():
	''' Guess the a random number '''
	number = range(1,100)
	# for num in range(1,100):
	# 	number.append(num)
	return random.choice(number)
#code easy mode
def easy():
	answer = random_number()
	#print (f"The answer is: {answer}.")
	global EASY_LIVES
	is_game_over = False
	while not is_game_over:
		print(f"You have {EASY_LIVES} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		if guess == answer:
			print(f"You got it! The answer was {answer}")
			is_game_over = True
		else:
			EASY_LIVES -= 1
			if guess > answer and EASY_LIVES != 0:
				print("Too High")
				print("Guess again.")
			elif guess < answer and EASY_LIVES != 0:
				print("Too Low")
				print("Guess again.")
		if EASY_LIVES == 0:
			is_game_over = True
			print("You've run out of guesses, you lose.")
#code hard mode				
def hard ():
	answer = random_number()
	global HARD_LIVES
	is_game_over = False
	while not is_game_over:
		print(f"You have {HARD_LIVES} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		if guess == answer:
			print(f"You got it! The answer was {answer}")
			is_game_over = True
		else:
			HARD_LIVES -= 1
			if guess > answer and HARD_LIVES != 0:
				print("Too High")
				print("Guess again.")
			elif guess < answer and HARD_LIVES != 0:
				print("Too Low")
				print("Guess again.")
		if HARD_LIVES == 0:
			is_game_over = True
			print("You've run out of guesses, you lose.")


#Print the Greatting
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if choice == "easy":
	easy()
else:
	hard()

#Teachers CODE
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
