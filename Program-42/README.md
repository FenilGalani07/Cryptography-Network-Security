# Character Occurrence Counter

Welcome to the Character Occurrence Counter! This Python program allows you to count how many times a specific character appears in a given string. It's a simple yet useful tool for text analysis and manipulation.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Counts occurrences of a specified character in a user-provided string.
- Validates input to ensure only a single character is counted.
- User-friendly interface for easy interaction.

## How It Works

The program defines a function `count_character_occurrences` that iterates through each character in the input string and increments a counter whenever it finds a match with the specified character. The result is then displayed to the user.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter a string when prompted.
4. Enter the character you want to count.

### Example

```python
def count_character_occurrences(input_string, character):
    count = 0
    for char in input_string:
        if char == character:
            count += 1
    return count

if __name__ == "__main__":
    user_string = input("Enter a string: ")
    user_character = input("Enter the character to count: ")
    if len(user_character) != 1:
        print("Please enter a single character.")
    else:
        occurrences = count_character_occurrences(user_string, user_character)
        print(f"The character '{user_character}' occurs {occurrences} times in the string.")
```

### Sample Output

```
Enter a string: Hello, World!
Enter the character to count: o
The character 'o' occurs 2 times in the string.
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

