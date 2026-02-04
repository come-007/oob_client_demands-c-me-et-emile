# ==========================================
# CLIENT MANAGEMENT - EDUCATIONAL VERSION
# ==========================================
# This script manages client data in a text file.
# Students: Notice how the code is grouped into logical sections.
# Each section could eventually become a function!
FILENAME = "clients.txt"

def ajouter_client():
    name = input("- Name: ")
    email = input("- Email: ")
    
    f = open(FILENAME, "r")
    lignes = f.readlines()
    f.close()
    
    new_id = len(lignes)
    
    f = open(FILENAME, "a")
    f.write(f"{new_id},{name},{email}\n")
    f.close()
    print(f"Client enregistré avec l'ID {new_id}")

def afficher_liste():
    print("\n--- CLIENTS LIST ---")
    f = open(FILENAME, "r")
    data = f.readlines()[1:] 
    f.close()
    
    clients = [line.strip().split(",") for line in data]
    
    for c in clients:
        if len(c) >= 3:
            print(f"ID: {c[0]} | Name: {c[1]} | Email: {c[2]}")

def menu():
    while True:
        print("\n1. Add a New client\n2. View all clients\n3. Exit Program")
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

menu()