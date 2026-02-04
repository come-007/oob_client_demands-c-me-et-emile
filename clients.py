# ==========================================
# CLIENT MANAGEMENT - EDUCATIONAL VERSION
# ==========================================
# This script manages client data in a text file.
# Students: Notice how the code is grouped into logical sections.
# Each section could eventually become a function!
import os

FILENAME = "clients.txt"

def setup_db():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            f.write("id,name,email\n")

def ajouter_client():
    name = input("- Name: ")
    email = input("- Email: ")
    with open(FILENAME, "r") as f:
        lignes = f.readlines()
    new_id = len(lignes)
    with open(FILENAME, "a") as f:
        f.write(f"{new_id},{name},{email}\n")
    print(f"client enregistred with the ID {new_id}")

def afficher_liste():
    print("\n--- CLIENTS LIST ---")
    with open(FILENAME, "r") as f:
        data = f.readlines()[1:] 
    

    clients = [line.strip().split(",") for line in data]
    
    for c in clients:
        if len(c) >= 3:
            print(f"ID: {c[0]} | Name: {c[1]} | Email: {c[2]}")

def menu():
    setup_db()
    while True:
        print("\n" + "="*25 + "\n1. Add a New clients\n2. View all clients\n3. Exit Program\n" + "="*25)
        choix = input("Action : ")
        if choix == "1":
            ajouter_client()
        elif choix == "2":
            afficher_liste()
        elif choix == "3":
            print("Goodbye")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    menu()  