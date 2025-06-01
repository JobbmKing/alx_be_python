# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start building the message
match priority:
    case "high":
        priority_text = "high priority task"
    case "medium":
        priority_text = "medium priority task"
    case "low":
        priority_text = "low priority task"
    case _:
        priority_text = "task of unknown priority"

# Generate the final message
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority_text}. Consider completing it when you have free time.")

