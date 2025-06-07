import json
import csv

data = "contact.json"

def data_load():
    try:
        with open(data, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []



def saver(users):
    with open(data , "w") as file:
        json.dump(users, file, indent=4)
    
def add_new_contact(users):
    name = input("Enter Name: ")
    mobile_number = input("Enter mobile Number: ")
    email = input("Enter Email: ").lower()
    address = input("Enter address: ")
    validation = validate_phone_number(mobile_number)
    if validation is True:
        for i in users:
         if mobile_number == i["Phone"]:
              print("Phone number already exists!")
              return
         if email == i["Email"].lower():
              print("Email ID already exists!")
              return
        else:
            users.append({"Name": name, "Phone": mobile_number, "Email": email, "Address": address})
            saver(users)
            print("Contact added successfully!")
    else:
        print(f"Invalid mobile number: {validation}")
    



def search_contact(users):
    pass
    search = input("Enter number/Name for search: ").lower()
    for i in users:
        if search in i["Name"].lower() or search in  i["Phone"]:
                    for k, v in i.items():
                       print(f"{k}   : {v}")
                    print("-" * 35)
                    return
    else:
        print("NO CONTACT FOUND!")

          

def view_contacts(users):
    print("\n--- Contact List ---\n")
    for index,  contact in enumerate (users, start=1):
        print(index,"\n","-"*35)
        print(f"Name      : {contact['Name']}")
        print(f"Phone     : {contact['Phone']}")
        print(f"Email     : {contact['Email']}")
        print(f"Address   : {contact['Address']}")
        print("-" * 35)


def edit_contact(users):
    view_contacts(users)
    index = int(input("Enter index number for edit: "))
    if 1 <= index <= len(users):
        name = input("Enter New Name: ")
        mobile_number = input("Enter New mobile Number: ")
        email = input("Enter New Email: ").lower()
        address = input("Enter New address: ")
        validation = validate_phone_number(mobile_number)
        if validation is True:
         users[index-1] = ({"Name": name, "Phone": mobile_number, "Email": email, "Address": address})
         saver(users)
         print("Contact EDIT successfully!")
        else:
            print(f"Invalid mobile number: {validation}")
    else:
        print("Please Enter Correct contact index.")


def delete_contact(users):
    view_contacts(users)
    index = int(input("Enter index number for delete the contact:  "))
    if 1 <= index <= len(users):
        users.pop(index - 1)
        saver(users)
        print("*" * 35)
        print("Contact deleted successfully!")
    else:
        print("Please enter correct index value...")

def validate_phone_number(number):
    try:
        if number.isdigit():
            if len(number) == 10:
                if number[0] in ['6', '7', '8', '9']:
                    return True
                else:
                    return "Plese start with 6,7,8,9"
            else:
                return "Please enter a 10-digit mobile number"
        else:
            return "Please enter digits only."

    except Exception as e:
        return f"ERROR: {e}"
    

def export_to_csv(users):
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Address"])
        for i in users:
           print(i)
           writer.writerow([i["Name"], i["Phone"], i["Email"], i["Address"]])
           print("yes")

    print("Contacts exported to CSV successfully!")
        
def main():
    users = data_load()
    while True:
        print("\tWELCOME TO -- Contact Book --\n\t    | CREATED By MOHIT |")
        print("-"*40)
        print("ENTER 1 FOR VIEW ALL CONTACTS.")
        print("-"*40)
        print("ENTER 2 FOR ADD NEW CONTACT.")
        print("-"*40)
        print("ENTER 3 FOR EDIT CONTACT.")
        print("-"*40)
        print("ENTER 4 FOR SEARCH A CONTACT.")
        print("-"*40)
        print("ENTER 5 FOR DELETE A CONTACT.")
        print("*"*40)
        print("ENTER 6 FOR export in CSV.")
        print("*"*40)
        print("ENTER 7 FOR EXIT")
        print("*"*40)
        user_input = int(input("ENTER YOUR INPUT --> "))

        if user_input == 1:
            view_contacts(users)
        elif user_input == 2:
            add_new_contact(users)
        elif user_input == 3:
            edit_contact(users)
        elif user_input == 4:
            search_contact(users)
        elif user_input == 5:
            delete_contact(users)
        elif user_input == 6:
            export_to_csv(users)
        elif user_input == 7:
            print('='*30)
            print("APP EXIT, THANKS FOR USING")
            print('='*30)
            break
        else:
            ("PLEASE ENTER A VALID INPUT...")

if __name__ == "__main__":
    main()

