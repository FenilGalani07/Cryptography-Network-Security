# Whitespace Trimmer

Welcome to the **Whitespace Trimmer** program! This Python script removes leading and trailing whitespace from a given string. It's a simple utility for text formatting and cleaning.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Trims leading and trailing whitespace from a string.
- Simple and easy to use.
- Useful for text formatting and cleaning.

## How It Works

The program defines a function `trim_whitespace` that:
1. Takes a string as input.
2. Uses the `strip()` method to remove any leading and trailing whitespace.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the string with leading and/or trailing whitespace when prompted.

### Example

```python
def trim_whitespace(input_string):
    return input_string.strip()

if __name__ == "__main__":
    user_input = input("Enter a string with leading and/or trailing whitespace: ")
    trimmed_string = trim_whitespace(user_input)
    print(f"Trimmed String: '{trimmed_string}'")
```

### Sample Output

```
Enter a string with leading and/or trailing whitespace:   Hello, World!
Trimmed String: 'Hello, World!'
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

