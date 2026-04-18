import csv
from caesar import caesar_encrypt
 
 
def encrypt_single_pass(filename):
    with open(filename, 'r') as file:
        password = file.read().strip()
    encrypted = caesar_encrypt(password)
    with open(filename, 'w') as file:
        file.write(encrypted)
 
 
def encrypt_passwords_in_file(filename):
    with open(filename, 'r') as file:
        lector = csv.reader(file)
        rows = [row for row in lector if row]
 
    for i in range(1, len(rows)):
        rows[i][2] = caesar_encrypt(rows[i][2])
 
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
 
 
def change_password(filename, website, password):
    with open(filename, 'r') as file:
        lector = csv.reader(file)
        rows = [row for row in lector if row]
 
    found = False
    for row in rows:
        if row[0] == website:
            row[2] = caesar_encrypt(password)
            found = True
            break
 
    if not found:
        return False
 
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
 
    return True
 
 
def add_login(filename, website_name, username, password):
    encrypted = caesar_encrypt(password)
    with open(filename, 'a') as file:
        writer = csv.writer(file)
     