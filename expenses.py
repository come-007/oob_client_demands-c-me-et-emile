# ==========================================
# EXPENSE MANAGEMENT - EDUCATIONAL VERSION
# ==========================================
# This script tracks money outgoing from your business.
# Notice how the ADD and LIST logic repeats patterns from other scripts.

FILENAME = "expenses.txt"

# --- 1. INITIALIZATION ---
try:
    check_file = open(FILENAME, "r")
    check_file.close()
except FileNotFoundError:
    print("Creating expense database...")
    create_db = open(FILENAME, "w")
    create_db.write("id,category,amount,date,description\n")
    create_db.close()

# --- 2. MAIN USER INTERFACE LOOP ---
while True:
    print("\n" + "-"*30)
    print("      EXPENSE TRACKER")
    print("-"*30)
    print("1. Record a New Expense")
    print("2. View All Expenses")
    print("3. Return to Main OS")
    
    choice = input("Option: ")

    # --- 3. ADD EXPENSE SECTION ---
    if choice == '1':
        print("\nEntering expense data:")
        category = input("- Category (e.g. Rent, Internet): ")
        amount = input("- Amount: ")
        date = input("- Date (YYYY-MM-DD): ")
        desc = input("- Description: ")
        
        # Step: Calculate ID by counting existing entries
        f_read = open(FILENAME, "r")
        lines = f_read.readlines()
        f_read.close()
        entry_id = len(lines)
        
        # Step: Write the data line
        f_append = open(FILENAME, "a")
        # Format: id,category,amount,date,description
        data_line = str(entry_id) + "," + category + "," + amount + "," + date + "," + desc + "\n"
        f_append.write(data_line)
        f_append.close()
        
        print(f"SAVED: '{category}' expense recorded.")

    # --- 4. LIST EXPENSES SECTION ---
    elif choice == '2':
        print("\n--- RECORDED EXPENSES ---")
        
        f_view = open(FILENAME, "r")
        header = f_view.readline() # We don't need to print the header
        
        line = f_view.readline()
        while line:
            # Step: Use .split() to convert string to a list of data
            data = line.strip().split(",")
            
            if len(data) >= 5:
                # Assigning variables makes the print statement much cleaner!
                eid = data[0]
                cat = data[1]
                val = data[2]
                dt  = data[3]
                ds  = data[4]
                print(f"ID {eid:2} | {dt} | {cat:10} | ${val:>7} | {ds}")
            
            line = f_view.readline()
            
        f_view.close()
        print("-" * 30)

    # --- 5. EXIT ---
    elif choice == '3':
        print("Closing Expense Tracker...")
        break
    else:
        print("Error: Input 1, 2, or 3.")
