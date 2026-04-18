from password_manager import encrypt_passwords_in_file, change_password, add_login
 
print("Enter the CSV file name:")
filename = input()
 
encrypt_passwords_in_file(filename)
 
while True:
    print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
    option = input()
 
  
 
        space = entry.find(' ')
 
      
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
 
        

 
        space2 = rest.find(' ')
 
        if space2 == -1:
            
            continue
 
        username = rest[0:space2]
        password = rest[space2 + 1:]
 
        if len(password) < 12:
            
 
        add_login(filename, website, username, password)
        print("Login added.")
 
    
 
    else:
        print("Invalid option selected!")
 