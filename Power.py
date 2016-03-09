def to_power(base, exp):

# This will count how many times the base is multiplied by itself
	count = 0
	next = 1
	
		
# This will multiply the base by itself equal to the value of the exponent
	while int(count) < int(exp):
		next = int(base) * next
		count += 1	
	
	return next


 ### Main program below ###


# User inputs Base and Exponent
base = raw_input("Enter a base: ")
exp = raw_input("Enter an exponent: ")


answer = to_power(base, exp)

print("The answer is {}".format(answer))
