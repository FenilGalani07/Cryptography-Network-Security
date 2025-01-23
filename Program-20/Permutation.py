# permutations.py

from itertools import permutations

def find_permutations(arr):
    return list(permutations(arr))

if __name__ == "__main__":
    input_list = input("Enter numbers separated by commas: ")
    input_list = [int(x.strip()) for x in input_list.split(',')]

    result_permutations = find_permutations(input_list)

    print("All permutations:")
    for perm in result_permutations:
        print(perm)