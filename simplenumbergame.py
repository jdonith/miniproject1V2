import random
import math

#User inputs
lower = int(input("Enter a number between 1 & 5: "))
upper = int(input("Enter a number between 25 & 30: "))

#Generating random number between
r = random.randint(lower, upper)
print("\n\tTry to guess it in less than",
	round(math.log(upper - lower + 1, 2)),
	"guesses!\n")

# Initializing the number of guesses.
count = 0


while count < math.log(upper - lower + 1, 2):
	count += 1

	
	guess = int(input("Guess a number: "))


	if r == guess:
		print("Congratulations you did it in",
			count, "tries")
		#Loop will break if guessed
		break
	elif r > guess:
		print("You guessed too small!")
	elif r < guess:
		print("You Guessed too high!")

# If more than the allowed number of guesses
if count > math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % r)
	print("\tYou can do better! Play again!")

