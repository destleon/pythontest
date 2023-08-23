hold_data = {}

while True:
    print("Contact Menu")
    print("1. Add contact")
    print("2. Display Contact")
    print("3. Delete Contact")
    print("4. Exit Contact")

    response = input("Please enter 1 or 2 or 3 or 4: ")

    if response == "1":
        contact_name = input("Please enter the contact name: ")
        contact_no = input("Please enter the contact number: ")
        hold_data[contact_name] = contact_no
        print(f"The Contact Name is: {contact_name} with the number {contact_no} has been saved successfully")

    elif response == "2":
        print("Display Contact")
        if hold_data:
            for contact_name, contact_no in hold_data.items():
                print(f"Contact Name: {contact_name} Contact No.: {contact_no}")
        else:
            print("No contact is saved for now")

    elif response == "3":
        contact_name_to_delete = input("Please enter the name you want to delete: ")

        if contact_name_to_delete in hold_data:
            del hold_data[contact_name_to_delete]
            print(f"The Contact Name: {contact_name_to_delete} is deleted successfully.")
        else:
            print(f"The Contact Name: {contact_name_to_delete} does not exist in the contact book.")

    elif response == "4":
        print("The Contact Book will exit.")
        break

    else:
        print("Please you have entered a wrong reply, check the input and check again.")
