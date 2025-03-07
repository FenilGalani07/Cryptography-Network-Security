# Remove Duplicates from List

Welcome to the **Remove Duplicates from List** program! This Python script efficiently removes duplicate elements from a list while preserving the original order of the elements. It's a handy tool for data cleaning and preprocessing.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Removes duplicate elements from a list.
- Maintains the original order of elements.
- Simple and easy-to-understand implementation.

## How It Works

The program defines a function `remove_duplicates` that iterates through the input list and uses a set to track seen elements. If an element has not been seen before, it is added to the result list. This ensures that only unique elements are included in the final output.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. The program will display the original list and the list after removing duplicates.

### Example

```python
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
```

### Sample Output

```
Original List: [1, 2, 3, 2, 4, 1, 5, 3]
List after removing duplicates: [1, 2, 3, 4, 5]
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani 
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

