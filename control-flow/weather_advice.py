# Objective: Utilize conditional statement to guide program execution
# based on user input regarding weather  conditions
# conditions = ["sunny", "rainy", "cold"]

#Prompt users for weather input
# add strip and lower to handle extra spaces and capitalization
weather = input("What's the weather like today? (sunny/rainy/cold):").strip().lower()

# provide clothing recommendations
#program will recommend different types of clothing

if weather == "sunny":
	print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
	print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
	print("Make sure to wear a warm coat and a scarf.")
else:
	print("Sorry, I don't have recommendations for this weather.")
