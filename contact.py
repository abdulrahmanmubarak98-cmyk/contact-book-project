import json
import os

while True:
    print("1. Add contact")
    print("2. view all contact")
    print("3. search contact")
    print("4. delete contact")
    print("0. exit")

    choice = input("Select an option: ")

    if choice == "1":
        Name = input("Enter contact name: ").lower()
        Phone_Number = int(input("Enter contact phone: "))
        Email = input("Enter contact email: ").lower()
        if os.path.exists("cont.json"):
            with open("cont.json", "r") as file:
                cont = json.load(file)

            cont.append({"Name": Name, "Phone_Number": Phone_Number, "Email": Email})

        else:
            cont = []

        with open("cont.json", "w") as file:
            json.dump(cont, file, indent = 4)

    elif choice == "2":
        with open("cont.json") as file:
            cont = json.load(file)

            for item in cont:
                print(item["Name"], item["Phone_Number"], item["Email"])

    elif choice == "3":
        with open("cont.json") as file:
            cont = json.load(file)

        search_name = input("Enter Name: ")
        found = False
        for contact in cont:
            
            if contact["Name"] == search_name:
                print(f"Name: {contact['Name']}")
                print(f"Phone_Number: {contact['Phone_Number']}")
                print(f"Email: {contact['Email']}")
                found = True
                break
        if not found:
            print("Contact not found")

    elif choice == "4":

        with open("cont.json", "r") as file:
                cont = json.load(file)

        found = False
        delete_name = input("Enter name: ")

        for contact in cont:
            if contact["Name"] == delete_name:
                    cont.remove(contact)
                    print("contact deleted")
                    found =  True
        if not found:
                print("No record found")

        with open("cont.json", "w") as file:
                json.dump(cont, file, indent = 4)
    elif choice == "0":
         print("Goodbye!")
         break

    else:
         print("invalid option")

        


       