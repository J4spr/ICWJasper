# import some stuff that I use for error handling
import sys

# create empty dictionary
contactlist = {}


def menu():
    """
    this is a  function to show the menu, it was a lot easier to make a function for that instead of typing it again
    """
    global userinput
    print("-------------------------------")
    print("Menu:")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Delete a contact")
    print("4. Edit contact")
    print("5. Search a contact")
    print("6. Sort contacts by: ")
    print("7. Quit")
    print("-------------------------------")
    userinput = input("Enter your choice (1/2/3/4/5): ")


def inputs():
    """
    this is a function to handle all the inputs
    """

    global inputname
    global inputlastname
    global inputtel
    global inputmail
    inputname = input("Give the name\n")
    inputlastname = input("give the last name\n")
    inputtel = input("give the number\n")
    inputmail = input("give the email\n")
    returnlist = [inputname, inputlastname, inputtel, inputmail]
    return returnlist


def addcontact(contactslist):
    """
    this is a function to add a contact to our dictionary

    :param: contactslist

    :return: a string that says that a given contactname is successfully added
    """
    # call input function
    inputs()
    # update dictionary with inputs
    contactslist.update({inputname: {"lastname": inputlastname, "phonenumber": inputtel, "email": inputmail.lower()}})
    returnvalue = f"{inputname} had been successfully added"
    return returnvalue


def viewcontacts(contactslist):
    """
    a function to view all the contacts that are in your contactslist

    :param contactslist:
    """
    # loop over all the contacts in the dictionary
    for key in contactslist:
        # print them out
        print(key, contactslist.get(key).get("lastname"), contactslist.get(key).get("phonenumber"))


def deletecontact(contactslist):
    """
    this deletes the given contact
    :param:
    contactslist

    :return:
    a string that says that the contact is successfully deleted
    """
    name = input("say name to remove: ")
    # if the name is in the dictionary delete it, if not return 'error'
    if name in contactslist:
        contactslist.pop(name)
    else:
        print("error")
    returnvalue = f"{name} has been successfully removed!"
    return returnvalue


def editcontact(contactslist):
    inputs()
    contactslist[inputname]["lastname"] = inputlastname
    contactslist[inputname]["phonenumber"] = inputtel
    contactslist[inputname]["email"] = inputmail.lower()
    returnvalue = f"{inputname} has been successfully edited"
    return returnvalue


def searchcontact(contactslist):
    name = input("Say a name you want to search\n")
    for i in contactslist:
        if i == name.lower():
            print(i, contactslist.get(i).get("lastname"), contactslist.get(i).get("phonenumber"),
                  contactslist.get(i).get("email"))
        else:
            for j in contactslist[i]:
                if contactslist[i][j] == name:
                    print(i, contactslist.get(i).get("lastname"), contactslist.get(i).get("phonenumber"),
                          contactslist.get(i).get("email"))


def sortcontacts(contactslist):
    """
    Sorts the contacts by a given field

    :param:
    the dictionary named contactlist

    :return:
    The dictionary sorted by the given field
    """
    valuelist = []
    field = input("What do you want to sort by?\n")
    for person in contactslist:
        personvalues = contactslist.get(person)
        value = personvalues.get(field)
        valuelist.append(value)
    sortedcontactlist = sorted(valuelist)

    for value in sortedcontactlist:
        for person in contactslist:
            if contactslist[person][field] == value:
                print(f"naam: {contactslist[person]}, {person, contactslist[person][field]}")


# main function
def main():
    while True:
        menu()
        match (int(userinput)):
            case 1:
                addcontact(contactlist)
            case 2:
                viewcontacts(contactlist)
            case 3:
                deletecontact(contactlist)
            case 4:
                editcontact(contactlist)
            case 5:
                searchcontact(contactlist)
            case 6:
                sortcontacts(contactlist)
            case 7:
                break
            case _:
                menu()


# use the proper starting of the program and even with error handling
if __name__ == '__main__':
    try:
        main()
    # if program is manually stopped, exit with exit code 130 (program manually stopped)
    except KeyboardInterrupt:
        print("\ninterrupted")
        sys.exit(130)
