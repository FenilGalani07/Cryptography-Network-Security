# Item Occurrence Counter

Welcome to the **Item Occurrence Counter** program! This Python script counts the number of times a specific item appears in a given list. It's a useful utility for data analysis and manipulation.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Counts the occurrences of a specified item in a list.
- Handles user input for the list and the item to count.
- Simple and easy to use.

## How It Works

The program defines a function `count_occurrences` that:
1. Takes a list and an item as input.
2. Uses the `count()` method of the list to count how many times the item appears.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the list of items and the item to count when prompted.

### Example

```python
def count_occurrences(input_list, item):
    return input_list.count(item)

if __name__ == "__main__":
    user_list = input("Enter a list of items (comma-separated): ").split(',')
    user_list = [item.strip() for item in user_list]

    item_to_count = input("Enter the item to count: ").strip()

    occurrences = count_occurrences(user_list, item_to_count)
    print(f"The item '{item_to_count}' occurs {occurrences} times in the list.")
```

### Sample Output

```
Enter a list of items (comma-separated): apple, banana, orange, apple, grape, banana
Enter the item to count: apple
The item 'apple' occurs 2 times in the list.
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

