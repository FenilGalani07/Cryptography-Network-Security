import os

def get_file_extension(file_name):

    return os.path.splitext(file_name)[1]

if __name__ == "__main__":
    file_name = input("Enter the file name (with extension): ")

    if os.path.isfile(file_name) or os.path.splitext(file_name)[1]:
        file_extension = get_file_extension(file_name)
        print(f"The file extension is: '{file_extension}'")
    else:
        print("The specified file name does not have a valid extension.")