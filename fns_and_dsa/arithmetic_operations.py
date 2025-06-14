#Arithmetic Operations Function
#define a function in this script that performs basic arithmetic operations
def perform_operation(num1, num2, operation):
	"""Perform arithmetic operation."""
	match operation:
		case "add":
			#return the addition of two values
			return num1 + num2
		case "subtract":
			#return the difference of two values
			return num1 - num2
		case "multiply":
			#multiply two values
			return num1 * num2
		case "divide":
			#divide two values
			if num2 == 0:
				print("Cant be divisible by 0")
			else:
				return num1 / num2
		case _:
			print("Invalid operation")
