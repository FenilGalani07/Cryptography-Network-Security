def lists_to_dict(keys, values):

    return dict(zip(keys, values))

if __name__ == "__main__":

    keys = input("Enter the keys (comma-separated): ").split(',')
    values = input("Enter the values (comma-separated): ").split(',')

    keys = [key.strip() for key in keys]
    values = [value.strip() for value in values]


    result_dict = lists_to_dict(keys, values)

    print("Resulting Dictionary:", result_dict)