def remove_duplicates(input_list):

    seen = set()

    result = []

    for item in input_list:

        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


if __name__ == "__main__":
    original_list = [1, 2, 3, 2, 4, 1, 5, 3]
    print("Original List:", original_list)
    unique_list = remove_duplicates(original_list)
    print("List after removing duplicates:", unique_list)
