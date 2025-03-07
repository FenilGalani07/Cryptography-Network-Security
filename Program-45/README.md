# Capitalize the First Character of a String

Welcome to the **Capitalize the First Character** program! This Python script takes a string input from the user and capitalizes the first character of that string. It's a simple utility for text formatting.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Capitalizes the first character of a given string.
- Handles empty strings gracefully.
- Simple and easy to use.

## How It Works

The program defines a function `capitalize_first_character` that checks if the input string is not empty. If it's not empty, it capitalizes the first character and concatenates it with the rest of the string. If the string is empty, it simply returns the original string.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the desired string when prompted.

### Example

```python
def capitalize_first_character(input_string):
    if input_string:  # Check if the string is not empty
        return input_string[0].upper() + input_string[1:]
    return input_string  # Return the original string if it's empty

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    capitalized_string = capitalize_first_character(user_input)
    print(f"Capitalized String: {capitalized_string}")
```

### Sample Output

```
Enter a string: hello world
Capitalized String: Hello world
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

