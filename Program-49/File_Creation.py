import os
from datetime import datetime

def get_file_dates(file_path):

    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)

    creation_time = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
    modification_time = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

    return creation_time, modification_time

if __name__ == "__main__":
    file_path = input("Enter the full path of the file: ")

    if os.path.isfile(file_path):
        creation_date, modification_date = get_file_dates(file_path)
        print(f"Creation Date: {creation_date}")
        print(f"Modification Date: {modification_date}")
    else:
        print("The specified path is not a valid file.")