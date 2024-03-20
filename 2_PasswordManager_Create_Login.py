import hashlib
import getpass

Manager={}

def create():
    username=input("Enter username: ")
    password=getpass.getpass("Enter password: ")
    hashed_pass=hashlib.sha256(password.encode()).hexdigest() #test
    Manager[username]=hashed_pass
    print("Succesfully saved!")

def login():
    username=input("Enter username: ")
    password=getpass.getpass("Enter password: ")
    hashed_pass=hashlib.sha256(password.encode()).hexdigest()
    if username in  Manager.keys() and Manager[username] == hashed_pass:
        print("Login succesfull! ")
    else:
        print("Login failed! Try again!")


def main():
    while True:
        choice = input("Enter 1 to create account, 2 to login, 3 to see all users or 0 to exit: ")
        if choice =="1":
            create()
        elif choice=="2":
            login()
        elif choice == "3":
            for username in Manager:
                hashed_pass=(Manager[username])
                print (f"Username is {username}")
                print(f" and password is {hashed_pass}")
        elif choice=="0":
                break
        else: print("Invalid choice!")

if __name__== "__main__":
    main()

