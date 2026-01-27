# ==========================================
# INVOICE MANAGEMENT - EDUCATIONAL VERSION
# ==========================================
# This script manages income from client invoices.
# Notice the repetitive pattern of opening and closing files.
# In a functional version, you would create a function for file operations!

FILENAME = "invoices.txt"

# --- 1. INITIALIZATION ---
try:
    file_test = open(FILENAME, "r")
    file_test.close()
except FileNotFoundError:
    init_db = open(FILENAME, "w")
    init_db.write("id,client_id,amount,date,description\n")
    init_db.close()

# --- 2. MAIN LOOP ---
while True:
    print("\n" + "!"*25)
    print("   INVOICE TRACKER")
    print("!"*25)
    print("1. Create New Invoice")
    print("2. List All Invoices")
    print("3. Exit Tracker")
    
    choice = input("Selection: ")

    # --- 3. ADD INVOICE SECTION ---
    if choice == '1':
        print("\nEnter invoice details:")
        client_id = input("- Client ID: ")
        amount = input("- Amount (e.g. 150.50): ")
        date = input("- Date (YYYY-MM-DD): ")
        desc = input("- Description: ")
        
        # Calculate ID
        file_read = open(FILENAME, "r")
        all_lines = file_read.readlines()
        file_read.close()
        new_id = len(all_lines)
        
        # Save to file
        file_append = open(FILENAME, "a")
        # Format: id,client_id,amount,date,description
        data_string = str(new_id) + "," + client_id + "," + amount + "," + date + "," + desc + "\n"
        file_append.write(data_string)
        file_append.close()
        
        print(f"Invoice #{new_id} saved successfully.")

    # --- 4. LIST INVOICES SECTION ---
    elif choice == '2':
        print("\n--- INVOICE HISTORY ---")
        
        file_view = open(FILENAME, "r")
        header = file_view.readline() # Burn the header
        
        current_data = file_view.readline()
        while current_data:
            # Use split to break the CSV line into a list
            parts = current_data.strip().split(",")
            
            if len(parts) >= 5:
                print(f"INV #{parts[0]} | Client {parts[1]} | ${parts[2]} | {parts[3]} | {parts[4]}")
            
            current_data = file_view.readline()
            
        file_view.close()
        print("-----------------------\n")

    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Try again.")
