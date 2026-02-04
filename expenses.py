# ==========================================
# EXPENSE MANAGEMENT - EDUCATIONAL VERSION
# ==========================================
# This script tracks money outgoing from your business.
# Notice how the ADD and LIST logic repeats patterns from other scripts.
import os

FILENAME = "expenses.txt"

# --- 1. INITIALIZATION ---
def initialize_db():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as create_db:
            create_db.write("id,category,amount,date,description\n")

# --- 3. ADD EXPENSE SECTION ---
def record_new_expense():
    print("\nEntering expense data:")
    category = input("- Category (e.g. Rent, Internet): ")
    amount = input("- Amount: ")
    date = input("- Date (YYYY-MM-DD): ")
    desc = input("- Description: ")
    
    # Step: Calculate ID by counting existing entries
    with open(FILENAME, "r") as f_read:
        lines = f_read.readlines()
    entry_id = len(lines)
    
    # Step: Write the data line
    with open(FILENAME, "a") as f_append:
        data_line = f"{entry_id},{category},{amount},{date},{desc}\n"
        f_append.write(data_line)
    
    print(f"SAVED: '{category}' expense recorded.")

# --- 4. LIST EXPENSES SECTION ---
def view_all_expenses():
    print("\n--- RECORDED EXPENSES ---")
    if not os.path.exists(FILENAME):
        return

    with open(FILENAME, "r") as f_view:
        lines = f_view.readlines()[1:] # Skip header

    # Functional approach: List comprehension to parse data
    expenses = [line.strip().split(",") for line in lines]
    
    for data in expenses:
        if len(data) >= 5:
            eid, cat, val, dt, ds = data[0], data[1], data[2], data[3], data[4]
            print(f"ID {eid:2} | {dt} | {cat:10} | ${val:>7} | {ds}")
    
    print("-" * 30)

# --- 2. MAIN USER INTERFACE LOOP ---
def main():
    initialize_db()
    while True:
        print("\n" + "-"*30 + "\n      EXPENSE TRACKER\n" + "-"*30)
        print("1. Record a New Expense\n2. View All Expenses\n3. Return to Main OS")
        
        choice = input("Option: ")

        if choice == '1':
            record_new_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            # --- 5. EXIT ---
            print("Closing Expense Tracker...")
            break
        else:
            print("Error: Input 1, 2, or 3.")

if __name__ == "__main__":
    main()