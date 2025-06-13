from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date  # Return it so we can reuse in future calculation

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Part 1
    current_date = display_current_datetime()

    # Part 2
    try:
        days_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

