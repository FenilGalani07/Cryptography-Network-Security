# reverse_array.py

def reverse_array(arr):

    return arr[::-1]

if __name__ == "__main__":
    try:

        input_elements = input("Enter elements separated by spaces: ")

        arr = list(map(int, input_elements.split()))

        # Reverse the array
        reversed_array = reverse_array(arr)

        print("Reversed array:", reversed_array)
    except ValueError:
        print("Please enter valid integers.")