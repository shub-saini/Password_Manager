import random
import string
from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# with open("key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def newpass():
    randpw=[random.choice(string.printable) for i in range(12)]
    password = ''.join(randpw)
    print(" Random password is:", password)
    print("Copy the above password to be used for a account")

while True:
    mode = input("Add password, view old passwords, new password (add/view/new), press q to quit:  ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "new":
        newpass()
    else:
        print("Invalid mode.")
        continue