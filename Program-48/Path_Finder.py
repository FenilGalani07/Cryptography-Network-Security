import os

def get_current_working_directory():

    return os.getcwd()

if __name__ == "__main__":
    current_directory = get_current_working_directory()
    print(f"The full path of the current working directory is: {current_directory}")