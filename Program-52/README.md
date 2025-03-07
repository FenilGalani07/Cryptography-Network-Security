# List to Dictionary Converter

Welcome to the **List to Dictionary Converter** program! This Python script converts two lists into a dictionary, where the first list serves as the keys and the second list serves as the values. It's a useful utility for data manipulation and organization.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Converts two lists into a dictionary.
- Handles input from the user for keys and values.
- Strips whitespace from keys and values for cleaner output.

## How It Works

The program defines a function `lists_to_dict` that:
1. Takes two lists as input.
2. Uses the `zip()` function to pair elements from both lists.
3. Converts the paired elements into a dictionary using the `dict()` constructor.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the keys and values as comma-separated strings when prompted.

### Example

```python
def lists_to_dict(keys, values):
    return dict(zip(keys, values))

if __name__ == "__main__":
    keys = input("Enter the keys (comma-separated): ").split(',')
    values = input("Enter the values (comma-separated): ").split(',')

    keys = [key.strip() for key in keys]
    values = [value.strip() for value in values]

    result_dict = lists_to_dict(keys, values)

    print("Resulting Dictionary:", result_dict)
```

### Sample Output

```
Enter the keys (comma-separated): name, age, city
Enter the values (comma-separated): Alice, 30, New York
Resulting Dictionary: {'name': 'Alice', 'age': '30', 'city': 'New York'}
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

