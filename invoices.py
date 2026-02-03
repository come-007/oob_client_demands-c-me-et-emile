# ==========================================
# INVOICE MANAGEMENT - SIMPLIFIED VERSION
# ==========================================

FILENAME = "invoices.txt"

# -------- Helper function --------
def read_invoices():
    """Returns a list of invoice rows (excluding header)."""
    with open(FILENAME, "r") as f:
        lines = f.readlines()[1:]  # ignore header
    return lines

def append_invoice(client_id, amount, date, desc):
    """Adds a new invoice to the file."""
    invoices = read_invoices()
    new_id = len(invoices) + 1

    with open(FILENAME, "a") as f:
        f.write(f"{new_id},{client_id},{amount},{date},{desc}\n")

    print(f"Invoice #{new_id} saved successfully.")


# -------- Initialization --------
try:
    with open(FILENAME, "r") as f:
        pass
except FileNotFoundError:
    with open(FILENAME, "w") as f:
        f.write("id,client_id,amount,date,description\n")


# -------- Main Loop --------
while True:
    print("\n" + "!"*25)
    print("   INVOICE TRACKER")
    print("!"*25)
    print("1. Create New Invoice")
    print("2. List All Invoices")
    print("3. Exit Tracker")

    choice = input("Selection: ")

    if choice == '1':
        print("\nEnter invoice details:")
        client_id = input("- Client ID: ")
        amount = input("- Amount: ")
        date = input("- Date (YYYY-MM-DD): ")
        desc = input("- Description: ")

        append_invoice(client_id, amount, date, desc)

    elif choice == '2':
        print("\n--- INVOICE HISTORY ---")

        for line in read_invoices():
            parts = line.strip().split(",")
            if len(parts) == 5:
                print(f"INV #{parts[0]} | Client {parts[1]} | ${parts[2]} | {parts[3]} | {parts[4]}")
        
        print("-----------------------\n")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Try again.")

    
