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
	temp_input = input("Enter the temperature (e.g., 100F or 37C): ").strip().upper()

	try:
		#extract numeric value and unit
		if temp_input.endswith('F'):
			value = float(temp_input[:-1])
			result = convert_to_celsius(value)
			print(f"{value}F is {round(result, 2)}C")

		elif temp_input.endswith('C'):
			value = float(temp_input[:-1])
			result = convert_to_fahrenheit(value)
			print(f"{value}C is {round(result, 2)}F")

		else:
			raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit")

	except ValueError as e:
		print(f"Invalid temperature. {e}")

if __name__ == "__main__":
	main()
