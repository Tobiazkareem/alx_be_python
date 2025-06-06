#Multiplication Table Generator

#Use a for loop to generate and print the multiplication table for a given number

#Prompt user for a number
number = int(input("Enter a number to see its multiplication table:"))

#Generate and print the Multiplication Table
#Use For Loop

for i in range(1, 11):
	product = number * i
	print(f"{number} * {i} = {product}")
