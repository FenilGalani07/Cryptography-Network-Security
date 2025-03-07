def get_last_element(input_list):

    if input_list:
        return input_list[-1]
    return None

if __name__ == "__main__":
    user_list = input("Enter a list of items (comma-separated): ").split(',')
    user_list = [item.strip() for item in user_list]

    last_element = get_last_element(user_list)

    if last_element is not None:
        print(f"The last element of the list is: {last_element}")
    else:
        print("The list is empty. Please enter some items.")