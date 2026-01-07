# =====================================================
# TASK 2: Personal Expense Tracker
# Author: M Saeed
#
# Description:
# This Python application helps users track their daily
# expenses. Users can add expenses, view daily/weekly/
# monthly summaries, visualize spending using bar and
# pie charts, and identify top spending categories.
# Expense data is stored locally using a CSV file.
# =====================================================
# Import required libraries
import csv                     # For reading and writing CSV files
import os                      # For file handling operations
from datetime import datetime  # For date handling
import pandas as pd            # For data analysis
import matplotlib.pyplot as plt # For data visualization

# Define CSV file name
FILE_NAME = "expenses.csv"

# -----------------------------------------------------
# Function to create CSV file if it does not exist
# -----------------------------------------------------
def initialize_file():
    # Check if file already exists
    if not os.path.exists(FILE_NAME):
        # Create a new CSV file
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header row
            writer.writerow(["Date", "Category", "Amount", "Description"])

# -----------------------------------------------------
# Function to add a new expense
# -----------------------------------------------------
def add_expense():
    # Take input from user
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    # Open CSV file in append mode
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write expense data into file
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")

# -----------------------------------------------------
# Function to load expense data using pandas
# -----------------------------------------------------
def load_data():
    # Read CSV file and convert Date column to datetime
    return pd.read_csv(FILE_NAME, parse_dates=["Date"])

# -----------------------------------------------------
# Function to show expense summary
# -----------------------------------------------------
def expense_summary(period):
    # Load data
    df = load_data()
    
    # Get today's date
    today = pd.to_datetime("today")

    # Filter data based on selected period
    if period == "daily":
        filtered_data = df[df["Date"] == today.normalize()]
    elif period == "weekly":
        filtered_data = df[df["Date"] >= today - pd.Timedelta(days=7)]
    elif period == "monthly":
        filtered_data = df[df["Date"].dt.month == today.month]

    # Display summarized expenses by category
    print(f"\n{period.upper()} EXPENSE SUMMARY")
    print(filtered_data.groupby("Category")["Amount"].sum())

# -----------------------------------------------------
# Function to visualize expenses
# -----------------------------------------------------
def visualize_expenses():
    # Load expense data
    df = load_data()

    # Group data by category
    category_total = df.groupby("Category")["Amount"].sum()

    # Create bar chart
    category_total.plot(kind='bar', title="Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

    # Create pie chart
    category_total.plot(kind='pie', autopct='%1.1f%%', title="Expense Distribution")
    plt.ylabel("")
    plt.show()

# -----------------------------------------------------
# Function to display top spending categories
# -----------------------------------------------------
def top_spending_categories():
    # Load data
    df = load_data()

    # Sort categories by total expense
    top_categories = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

    print("\nTop Spending Categories:")
    print(top_categories)

# -----------------------------------------------------
# Main function
# -----------------------------------------------------
def main():
    # Initialize CSV file
    initialize_file()

    # Display menu until user exits
    while True:
        print("\n====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. Daily Summary")
        print("3. Weekly Summary")
        print("4. Monthly Summary")
        print("5. Visualize Expenses")
        print("6. Top Spending Categories")
        print("7. Exit")

        # User choice
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            expense_summary("daily")
        elif choice == "3":
            expense_summary("weekly")
        elif choice == "4":
            expense_summary("monthly")
        elif choice == "5":
            visualize_expenses()
        elif choice == "6":
            top_spending_categories()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# -----------------------------------------------------
# Program execution starts here
# -----------------------------------------------------
if __name__ == "__main__":
    main()
