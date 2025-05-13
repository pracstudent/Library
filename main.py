import init_csvs  # creates CSV files if they don't exist

# main.py
from helpers import Helper

def menu():
    while True:
        print("\nLibrary Member Management")
        print("1. List members")
        print("2. Add a member")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            Helper.list_members()
        elif choice == '2':
            Helper.add_member()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    menu()
