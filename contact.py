import json
import os
while True:
    print("menu")
    print("1. Add contact")
    print("2. view all contacts")
    print("3. search contact")
    print("0. exit")

    choice = input("select an option!: ")
    if choice == "1":
        Name = input("Enter name: ").lower()
        phone = int(input("Enter phone number: "))
        email = input("Enter email: ").lower()
## using json read "r" write "w" 
# load and dump
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                contacts = json.load(file)

        contacts[Name] = {"phone": phone, "email": email}

        with open("contacts.json", "w") as file:
            json.dump(contacts, file)

    elif choice == "2":
        file = open("contacts.json", "r")
        contacts = json.load(file)
        for name, info in contacts.items():
            print(name, info["phone"], info["email"])
        file.close()

    elif choice == "3":
        name = input("Enter name: ")
        if name in contacts:
            print(contacts [name])
        else:
            print("contact not found")

    elif choice == "0":
        print("Goodbye, Have a nice day!")
        break

    else:
        print("invalid option")

    




