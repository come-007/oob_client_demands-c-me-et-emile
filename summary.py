# ==========================================
# FINANCIAL SUMMARY - Modified VERSION
# ==========================================
# This script "pulls it all together".
# It reads both Invoices and Expenses to calculate the Net Profit.
# Students: Observe how we reuse the file-reading pattern here!

INVOICE_DATA = "invoices.txt"
EXPENSE_DATA = "expenses.txt"


def sum_csv_amounts(filepath):
    """
    Reads CSV file with a header and sums the 3rd column .
    Returns 0.0 if file missing or invalid.
    """
    total = 0.0

    try:
        with open(filepath, "r") as file:
            next(file)  # skip header

            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 3:
                    try:
                        total += float(parts[2])
                    except ValueError:
                        print(f"[!] Invalid amount in file: {filepath}")

    except FileNotFoundError:
        print(f"[!] File not found: {filepath}")

    return total


# ---- PROCESSING ----
print("Reading Invoice data...")
income_total = sum_csv_amounts(INVOICE_DATA)

print("Reading Expense data...")
expense_total = sum_csv_amounts(EXPENSE_DATA)

profit_or_loss = income_total - expense_total


# ---- OUTPUT REPORT ----
print("\n" + "=" * 35)
print("      YEAR-TO-DATE SUMMARY")
print("=" * 35)
print(f"Total Gross Income:   ${income_total:10.2f}")
print(f"Total Business Costs: ${expense_total:10.2f}")
print("-" * 35)

if profit_or_loss >= 0:
    print(f"NET PROFIT:          +${profit_or_loss:10.2f}")
else:
    print(f"NET LOSS:            -${abs(profit_or_loss):10.2f}")

print("=" * 35 + "\n")
