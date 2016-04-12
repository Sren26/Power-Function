# Author : Sanford Ren
# Date: 4/12/16

# A revised recursive power function
def to_power(base, exp):
	if exp == 0:
		return 1
	answer = base * to_power(base, exp - 1)
	return answer

# This function below will ensure that the user only enters a float,
 # or else the program will return a error and prompt the user to try again
def float_input(prompt):
	answer = raw_input(prompt)
	try:
		return float(answer)
	except ValueError:
		return float_input("That wasn't a number. Try again: ")

# This function below will ensure that the user only enters a float,
 # or else the program will return a error and prompt the user to try again		
def int_input(prompt):
	answer = raw_input(prompt)
	try:
		return int(answer)
	except ValueError:
		return int_input("That wasn't a number. Try again: ")


# Main program below

uBase = float_input("Enter a base for a power function: ")

uExponent = int_input("Enter an exponent for a power function: ")

answer = to_power(uBase, uExponent)

print("{} to the power of {} is {}." .format(uBase, uExponent, answer))
