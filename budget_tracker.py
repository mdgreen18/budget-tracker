import csv
from collections import defaultdict

def load_expenses(csv_file):
    expenses = defaultdict(float)
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['Category']
            amount = float(row['Amount'])
            expenses[category] += amount
    return expenses

def display_summary(expenses):
    print("\n--- Expense Summary by Category ---")
    for category, total in expenses.items():
        print(f"{category}: ${total:.2f}")

if __name__ == "__main__":
    file = "sample_data.csv"
    data = load_expenses(file)
    display_summary(data)

