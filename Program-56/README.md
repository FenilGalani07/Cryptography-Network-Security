# Last Element Retriever

Welcome to the **Last Element Retriever** program! This Python script retrieves and displays the last element of a specified list. It's a simple utility for list manipulation and data retrieval.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Retrieves the last element from a given list.
- Handles user input for the list of items.
- Checks for empty lists and provides appropriate feedback.

## How It Works

The program defines a function `get_last_element` that:
1. Takes a list as input.
2. Uses negative indexing to access the last element of the list.
3. Returns the last element or `None` if the list is empty.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the list of items when prompted.

### Example

```python
def get_last_element(input_list):
    if input_list:
        return input_list[-1]
    return None

if __name__ == "__main__":
    user_list = input("Enter a list of items (comma-separated): ").split(',')
    user_list = [item.strip() for item in user_list]

    last_element = get_last_element(user_list)

    if last_element is not None:
        print(f"The last element of the list is: {last_element}")
    else:
        print("The list is empty. Please enter some items.")
```

### Sample Output

```
Enter a list of items (comma-separated): apple, banana, orange, grape
The last element of the list is: grape
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)
