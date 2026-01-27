# ==========================================
# FINANCIAL SUMMARY - EDUCATIONAL VERSION
# ==========================================
# This script "pulls it all together".
# It reads both Invoices and Expenses to calculate the Net Profit.
# Students: Observe how we reuse the file-reading pattern here!

INVOICE_DATA = "invoices.txt"
EXPENSE_DATA = "expenses.txt"

# Initialize our totals
income_total = 0.0
expense_total = 0.0

# --- 1. PROCESS INCOMES (INVOICES) ---
print("Reading Invoice data...")
try:
    inv_file = open(INVOICE_DATA, "r")
    # Skip the line with the words "id,client_id,amount..."
    inv_file.readline() 
    
    line = inv_file.readline()
    while line:
        # Step: Extract the amount from the line
        parts = line.strip().split(",")
        if len(parts) >= 3:
            amount_str = parts[2]
            income_total = income_total + float(amount_str)
        line = inv_file.readline()
        
    inv_file.close()
except FileNotFoundError:
    print("[!] No invoice file found. Total income is $0.")

# --- 2. PROCESS OUTGOINGS (EXPENSES) ---
print("Reading Expense data...")
try:
    exp_file = open(EXPENSE_DATA, "r")
    # Skip header
    exp_file.readline()
    
    line = exp_file.readline()
    while line:
        # Step: Extract the amount
        parts = line.strip().split(",")
        if len(parts) >= 3:
            amount_str = parts[2]
            expense_total = expense_total + float(amount_str)
        line = exp_file.readline()
        
    exp_file.close()
except FileNotFoundError:
    print("[!] No expense file found. Total expenses are $0.")

# --- 3. FINAL CALCULATION ---
profit_or_loss = income_total - expense_total

# --- 4. DISPLAY THE REPORT ---
print("\n" + "="*35)
print("      YEAR-TO-DATE SUMMARY")
print("="*35)
print(f"Total Gross Income:   ${income_total:10.2f}")
print(f"Total Business Costs: ${expense_total:10.2f}")
print("-" * 35)

if profit_or_loss >= 0:
    print(f"NET PROFIT:          +${profit_or_loss:10.2f}")
else:
    print(f"NET LOSS:            -${abs(profit_or_loss):10.2f}")

print("="*35 + "\n")
print("TIPS for Students:")
print("- Could you make a function that sums a specific CSV column?")
print("- How would you handle errors if a file is corrupted?")
