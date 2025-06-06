#Personal Daily Reminder

#Use of conditional statements, match case and loops
#to remind users about a single, priority task for the day
#based on time sensitivity

#prompt for a single task
#prompt for task description
task = input("Enter your task: ")

#prompt for task's priority
priority = input("Priority (high/medium/low): ").strip().lower()

#prompt for time bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

#process the task based on priority and time sensitivity
#using a match case statement

match priority:
	case "high":
		msg = f"{task} is a high priority task"
	case "medium":
		msg = f"Medium priority task - {task}"
	case "low":
		msg = f"{task} is a low priority task."
	case " ":
		print("Unknown priority")

#time bound urgency
if time_bound == "yes":
	print(f"Reminder: {msg} that requires immediate attention today!")
elif time_bound == "no":
	print(f"Note: {msg} Consider completing it when you have free time.")
else:
	print("No priority assigned")
