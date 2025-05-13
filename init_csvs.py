# import csv
# import os

# # Make sure the directory exists
# os.makedirs('csv', exist_ok=True)

# files = {
#     'librarians.csv': ['id', 'name', 'email'],
#     'members.csv':    ['id', 'name', 'membership_date'],
#     'items.csv':      ['id', 'title', 'author', 'status'],
#     'library.csv':    ['item_id', 'status', 'borrowed_by']
# }

# for fname, headers in files.items():
#     path = os.path.join('csv', fname)  # create full path like csv/librarians.csv
#     with open(path, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(headers)

# print("CSV files initialised in /csv directory.")

import csv
import os

# Make sure the directory exists
os.makedirs('csv', exist_ok=True)

files = {
    'librarians.csv': ['id', 'name', 'email'],
    'members.csv':    ['id', 'name', 'membership_date'],
    'items.csv':      ['id', 'title', 'author', 'status'],
    'library.csv':    ['item_id', 'status', 'borrowed_by']
}

for fname, headers in files.items():
    path = os.path.join('csv', fname)  # full path like csv/librarians.csv

    if os.path.exists(path):
        print(f"{fname} already exists. Skipping.")
        continue

    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        print(f"{fname} created.")

print("CSV setup complete.")
