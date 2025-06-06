#Drawing patterns with Nested Loops
# Utilize while loops and nested for loops to draw a simple test-based pattern

#prompts user for pattern size - postive integer
length = int(input("Enter the size of the pattern:"))

#Initialize a row counter
row = 0

#Draw the pattern:
#use a while loop to iterate each row of the pattern
while row < length:
	for col in range(length):
		print("*", end="")
#After completing each row, print a newline character to move to the next row
	print()
	row += 1
