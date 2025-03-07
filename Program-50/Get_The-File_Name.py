import os

def get_file_name(file_path):

    return os.path.basename(file_path)

if __name__ == "__main__":
    file_path = input("Enter the full path of the file: ")

    if os.path.isfile(file_path):
        file_name = get_file_name(file_path)
        print(f"The file name is: {file_name}")
    else:
        print("The specified path is not a valid file.")