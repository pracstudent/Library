# helpers.py
import csv
import os

class Helper:
    @staticmethod
    def list_members():
        path = os.path.join('csv', 'members.csv')

        if not os.path.exists(path):
            print("No members found. File does not exist.")
            return

        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"{row['id']}: {row['name']} ({row['membership_date']})")
    @staticmethod
    def add_member():
        mid  = input("ID: ").strip()
        name = input("Name: ").strip()
        date = input("Date (YYYY-MM-DD): ").strip()

        path = os.path.join('csv', 'members.csv')

        # Ensure the directory exists
        os.makedirs('csv', exist_ok=True)

        # Create the file with headers if it doesn't exist
        if not os.path.exists(path):
            f = open(path, 'w', newline='', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow(['id', 'name', 'membership_date'])
            f.close()

        # Append the new member
        f = open(path, 'a', newline='', encoding='utf-8')
        writer = csv.writer(f)
        writer.writerow([mid, name, date])
        f.close()

        print("Member added.")
    # def add_member():
    #     mid  = input("ID: ")
    #     name = input("Name: ")
    #     date = input("Date (YYYY-MM-DD): ")
        
    #     path = os.path.join('csv', 'members.csv')

    #     # Create file with header if it doesn't exist
    #     if not os.path.exists(path):
    #         os.makedirs('csv', exist_ok=True)
    #         with open(path, 'w', newline='', encoding='utf-8') as f:
    #             writer = csv.writer(f)
    #             writer.writerow(['id', 'name', 'membership_date'])

    #     with open(path, 'a', newline='', encoding='utf-8') as f:
    #         writer = csv.writer(f)
    #         writer.writerow([mid, name, date])
        
    #     print("Member added.")
