# remove_duplicates.py

def remove_duplicates(elements):

    seen = set()
    unique_elements = []

    for element in elements:
        if element not in seen:
            seen.add(element)
            unique_elements.append(element)

    return unique_elements

if __name__ == "__main__":
    try:

        input_elements = input("Enter elements separated by spaces: ")
        elements = input_elements.split()

        unique_elements = remove_duplicates(elements)

        print("Unique elements:", ' '.join(unique_elements))
    except Exception as e:
        print("An error occurred:", e)
