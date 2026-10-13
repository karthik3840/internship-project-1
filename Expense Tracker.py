print("=" * 40)
print("        EXPENSE TRACKER")
print("=" * 40)
total = 0
while True:
    user_input = input("Enter expense (or type 'quit' to finish): ")

    if user_input.lower() == "quit":
        break

    try:
        expense = int(user_input)

        if expense < 0:
            print("Expense cannot be negative.")
            continue
        total += expense
        print(f"Current Total: ${total}")

    except ValueError:
        print("Invalid Data! Please enter a valid number.")

print("\n" + "=" * 40)
print(f"Final Total Spent: ${total}")
print("Thank you for using Expense Tracker!")
print("=" * 40)