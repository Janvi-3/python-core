import json
import os
from datetime import datetime

EXPENSES_FILE_PATH = r"C:\Users\Dell\OneDrive\Desktop\python project\Expense_Tracker\expenses.txt"

def load_expenses():
    if os.path.exists(EXPENSES_FILE_PATH):
        try:
            with open(EXPENSES_FILE_PATH, "r") as f:
                return json.load(f)  
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    else:
        return []

def save_expenses(expenses):
    with open(EXPENSES_FILE_PATH, "w") as f:
        json.dump(expenses, f, indent=4) 

def add_expenses(expenses):
    print("---> ADD EXPENSES <---")
    
    description = ""
    while not description:
        description = input("Enter Description: ")
        if not description:
            print("Description cannot be empty!")

    amount = None  
    while amount is None:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive.")
                amount = None
        except ValueError:
            print("Please enter a valid number!")

    categories = ["Food", "Transport", "Housing", "Entertainment", "Other"]
    print("\nCategories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    category = ""
    while not category:
        try:
            choice = int(input("Select category (1-5): "))
            if 1 <= choice <= 5:
                category = categories[choice - 1]
            else:
                print("Please select between 1-5!")
        except ValueError:
            print("Please enter a number!")

    new_expense = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "description": description,
        "amount": amount,
        "category": category
    }
        
    expenses.append(new_expense)
    save_expenses(expenses)
    print("\nExpense added successfully!")

def view_all_expenses(expenses):
    print("---> All Expenses <---")
    if not expenses:
        print("No expenses recorded yet!")
        return
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. [{expense['date']}] {expense['description']:20} ${expense['amount']:8.2f} ({expense['category']})")

def view_category_summary(expenses):
    print("\n--- Spending by Category ---")
    if not expenses:
        print("No expenses recorded yet!")
        return
    
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        category_totals[category] = category_totals.get(category, 0) + expense['amount']
    
    for category, total in sorted(category_totals.items()):
        print(f"{category:15}: ${total:.2f}")
def view_total_spending(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Spending: ${total:.2f}")

def main():
    
    print("\n=== Simple Expense Tracker ===")
    expenses = load_expenses()
    
    while True:
        print("\nMenu Options:")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Spending by Category")
        print("4. View Total Spending")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            add_expenses(expenses)  
        elif choice == "2":
            view_all_expenses(expenses)
        elif choice == "3":
            view_category_summary(expenses)  
        elif choice == "4":
            view_total_spending(expenses)  
        elif choice == "5":
            print("\nGoodbye! Your data has been saved.")
            break
        else:
            print("Invalid choice! Please enter 1-5.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
