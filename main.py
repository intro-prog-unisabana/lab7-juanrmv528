from password_manager import encrypt_passwords_in_file, change_password, add_login
 
print("Enter the CSV file name:")
filename = input()
 
encrypt_passwords_in_file(filename)
 

 
  
 
        space = entry.find(' ')
 
      

            continue
 
        result = change_password(filename, website, new_password)
 
        if result == False:
            print("Website not found! Operation failed.")
     
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
 