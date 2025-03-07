def merge_dictionaries(dict1, dict2):

    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

if __name__ == "__main__":
    # Example dictionaries
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'd': 4}

    merged_dict = merge_dictionaries(dict1, dict2)
    print("Merged Dictionary:", merged_dict)