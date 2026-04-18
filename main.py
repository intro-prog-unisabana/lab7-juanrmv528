from password_manager import encrypt_passwords_in_file, change_password, add_login
 
print("Enter the CSV file name:")
filename = input()
 
encrypt_passwords_in_file(filename)
 
while True:
    print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
    option = input()
 
    if option == '1':
        print("Enter the website and the new password:")
        entry = input()
 
        space = entry.find(' ')
 
        if space == -1:
            print("Input is in the wrong format!")
            continue
 
        website = entry[0:space]
        new_password = entry[space + 1:]
 
        if len(new_password) < 12:
            print("Password is too short!")
            continue
 
        result = change_password(filename, website, new_password)
 
        if result == False:
            print("Website not found! Operation failed.")
        else:
            print("Password changed.")
 
    elif option == '2':
        print("Enter the website, username, and password:")
        entry = input()
 
        space1 = entry.find(' ')
 
        if space1 == -1:
            print("Input is in the wrong format!")
            continue
 
        website = entry[0:space1]
        rest = entry[space1 + 1:]
 
        space2 = rest.find(' ')
 
        if space2 == -1:
            
            continue
 
        username = rest[0:space2]
        password = rest[space2 + 1:]
 
        if len(password) < 12:
            print("Password is too short!")
            continue
 
        add_login(filename, website, username, password)
        print("Login added.")
 
    elif option == '3':
        break
 
    else:
        print("Invalid option selected!")
 