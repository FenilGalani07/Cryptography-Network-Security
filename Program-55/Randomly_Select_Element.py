import random

def randomly_select_element(input_list):

    return random.choice(input_list)

if __name__ == "__main__":
    user_list = input("Enter a list of items (comma-separated): ").split(',')
    user_list = [item.strip() for item in user_list]

    if user_list:
        selected_item = randomly_select_element(user_list)
        print(f"Randomly selected item: {selected_item}")
    else:
        print("The list is empty. Please enter some items.")