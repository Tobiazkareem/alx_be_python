#explore date and time
from datetime import datetime, timedelta

def display_current_datetime():
	current_date = datetime.now()
	formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
	print(f"Current date and time: {formatted_date}")

#calculate a future date
def calculate_future_date(days):
	current_date = datetime.now()
	future_date = current_date + timedelta(days=days)
	print(f"Date after {days} days: {future_date.strftime('%Y-%m-%d')}")

def  main():
	display_current_datetime()

	try:
		days = int(input("Enter the number of days to add to the current date: "))
		calculate_future_date(days)
	except ValueError:
		print("Please enter a valid integer for days.")

if __name__ == "__main__":
	main()
