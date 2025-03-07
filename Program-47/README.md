# Digit Counter

Welcome to the **Digit Counter** program! This Python script counts the number of digits present in a given integer. It's a simple utility for numerical analysis and data validation.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Counts the number of digits in a given integer.
- Handles negative numbers gracefully.
- Simple and easy to use.

## How It Works

The program defines a function `count_digits` that:
1. Takes an integer as input.
2. Converts the number to its absolute value and then to a string.
3. Counts the length of the string representation to determine the number of digits.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the desired number when prompted.

### Example

```python
def count_digits(number):
    return len(str(abs(number)))  # Use abs to handle negative numbers

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        digit_count = count_digits(user_input)
        print(f"The number of digits in {user_input} is: {digit_count}")
    except ValueError:
        print("Please enter a valid integer.")
```

### Sample Output

```
Enter a number: -12345
The number of digits in -12345 is: 5
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

