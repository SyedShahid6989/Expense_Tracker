expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)
        print("Expense added successfully!")

    elif choice == "2":
        print("Expenses:", expenses)

    elif choice == "3":
        total = sum(expenses)
        print("Total Spending =", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")