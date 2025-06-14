#converts temp between Calcius and Fahrenheit
# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
	"""Convert fahrenheit to celsius using the global conversion factory."""
	return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
	"""Convert celsius to fahrenheit using global conversion factor."""
	return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
	try:
		temp_input = input("Enter the temperature to convert: ").strip().upper()
		unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
		
		#extract numeric value and unit
		value = float(temp_input)

		if unit = 'F':
			result = convert_to_celsius(value)
			print(f"{value}F is {round(result, 2)}C")

		elif unit = 'C':
			result = convert_to_fahrenheit(value)
			print(f"{value}C is {round(result, 2)}F")

		else:
			raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit")

	except ValueError as e:
		print(f"Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
	main()
