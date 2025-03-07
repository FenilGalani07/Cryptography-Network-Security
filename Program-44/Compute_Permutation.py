import itertools

def compute_permutations(input_string):

    permutations = itertools.permutations(input_string)


    unique_permutations = set([''.join(p) for p in permutations])

    return unique_permutations


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = compute_permutations(user_input)
    print(f"All unique permutations of '{user_input}':")
    for perm in sorted(result):
        print(perm)