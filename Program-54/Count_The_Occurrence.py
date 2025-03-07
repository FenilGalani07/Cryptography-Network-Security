def count_occurrences(input_list, item):

    return input_list.count(item)

if __name__ == "__main__":

    user_list = input("Enter a list of items (comma-separated): ").split(',')
    user_list = [item.strip() for item in user_list]

    item_to_count = input("Enter the item to count: ").strip()

    occurrences = count_occurrences(user_list, item_to_count)
    print(f"The item '{item_to_count}' occurs {occurrences} times in the list.")