import pandas as pd
from datetime import datetime
import os

# File name
file_name = "expenses.csv"


# Create CSV file if it does not exist
if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])
    df.to_csv(file_name, index=False)


# Function to add an expense
def add_expense():

    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format!")
        return

    category = input("Enter category (Food/Travel/Shopping etc.): ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be positive!")
            return

    except ValueError:
        print("Please enter a valid amount!")
        return

    # Store expense in dictionary
    new_expense = {
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount
    }

    # Read old expenses
    df = pd.read_csv(file_name)

    # Add new expense
    df.loc[len(df)] = new_expense

    # Save expenses in CSV file
    df.to_csv(file_name, index=False)

    print("\nExpense saved successfully!")


# Function to view all expenses
def view_expenses():

    df = pd.read_csv(file_name)

    if df.empty:
        print("\nNo expenses found!")
    else:
        print("\n------ ALL EXPENSES ------")
        print(df.to_string(index=False))

        total = df["Amount"].sum()
        print("\nTotal expenses:", total)


# Function for category-wise summary
def category_summary():

    df = pd.read_csv(file_name)

    if df.empty:
        print("\nNo expenses found!")
    else:
        print("\n------ CATEGORY WISE SUMMARY ------")

        summary = df.groupby("Category")["Amount"].sum()

        print(summary)

        print("\nTotal expenses:", df["Amount"].sum())


# Function for monthly summary
def monthly_summary():

    df = pd.read_csv(file_name)

    if df.empty:
        print("\nNo expenses found!")
    else:
        print("\n------ MONTHLY SUMMARY ------")

        df["Date"] = pd.to_datetime(df["Date"])

        df["Month"] = df["Date"].dt.strftime("%Y-%m")

        summary = df.groupby("Month")["Amount"].sum()

        print(summary)

        print("\nTotal expenses:", df["Amount"].sum())


# Main program
while True:

    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Wise Summary")
    print("4. Monthly Summary")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        monthly_summary()

    elif choice == "5":
        print("\nThank you for using Personal Expense Tracker!")
        break

    else:
        print("\nInvalid choice! Please try again.")