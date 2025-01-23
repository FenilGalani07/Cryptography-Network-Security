# sort_array.py

def sort_array(arr):

    return sorted(arr)

if __name__ == "__main__":
    try:

        input_elements = input("Enter elements separated by spaces: ")

        arr = list(map(int, input_elements.split()))

        # Sort the array
        sorted_array = sort_array(arr)

        print("Sorted array:", sorted_array)
    except ValueError:
        print("Please enter valid integers.")