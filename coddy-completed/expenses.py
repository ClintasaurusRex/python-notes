

print("Welcome to the Daily Expense Tracker!\n\nMenu:")
options = [
    "Add a new expense",
    "View all expenses",
    "Calculate total and average expense",
    "Clear all expenses",
    "Exit"
]
expenses = [100, 200, 300]
for index, option in enumerate(options):
  print(f"{index + 1}. {option}")

while True:
  choice = int(input("Enter your choice (1-5): "))
  if choice == 5:
    print('Exiting the Daily Expense Tracker. Goodbye!')
    break
  elif choice == 1:
    option1 = float(input())
    expenses.append(option1)
    print('Expense added successfully!')
  elif choice == 2:
    if not expenses:
      print('No expenses recorded yet.')
    else:
      print("Your expenses:")
      for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense}")
  elif choice == 3:
    if not expenses:
      print("No expenses recorded yet.")
    else:
      total = float(sum(expenses))
      average = total / len(expenses)
      print(f"Total expense: {total}\nAverage expense: {average}")
  elif choice == 4:
    expenses.clear()
    print("All expenses cleared.")
  else:
    if choice < 1 or choice > 5:
      print("Invalid choice. Please try again.")